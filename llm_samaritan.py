import requests
import re
import time
import json
import os
import datetime

# ===== CONFIGURATION =====
TEST_MODE = True  # Set to True for testing
MAX_REPOS_TO_CHECK = 20 if TEST_MODE else 100
VERBOSE_LOGGING = True
DRY_RUN = True  # Don't actually create issues

# Your GitHub Token
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
VALID_KEYS_FILE = "valid_llm_keys.txt"
INVALID_KEYS_FILE = "invalid_llm_keys.txt"
FINDINGS_REPORT = "llm_keys_report.md"

# Headers for GitHub API requests
HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {GITHUB_TOKEN}" if GITHUB_TOKEN else None,
    "X-GitHub-Api-Version": "2022-11-28"
}

# Regex patterns specifically for LLM API keys
LLM_KEY_PATTERNS = [
    # OpenAI API Keys
    re.compile(r'sk-[A-Za-z0-9]{48}'),  # Standard OpenAI API key format
    re.compile(r'OPENAI_API_KEY\s*=\s*[\'"]([^\'"]+)[\'"]'),  # OPENAI_API_KEY assignments
    re.compile(r'openai\.api_key\s*=\s*[\'"]([^\'"]+)[\'"]'),  # openai.api_key assignments
    
    # Google Gemini/PaLM API Keys
    re.compile(r'AIza[0-9A-Za-z-_]{35}'),  # Standard Google AI API key format
    re.compile(r'GEMINI_API_KEY\s*=\s*[\'"]([^\'"]+)[\'"]'),  # GEMINI_API_KEY assignments
    re.compile(r'PALM_API_KEY\s*=\s*[\'"]([^\'"]+)[\'"]'),  # PALM_API_KEY assignments
    re.compile(r'GOOGLE_API_KEY\s*=\s*[\'"]([^\'"]+)[\'"]'),  # GOOGLE_API_KEY assignments

    # Anthropic API Keys
    re.compile(r'sk-ant-[A-Za-z0-9]{48}'),  # Anthropic Claude API key format
    re.compile(r'ANTHROPIC_API_KEY\s*=\s*[\'"]([^\'"]+)[\'"]'),  # ANTHROPIC_API_KEY assignments
    
    # Cohere API Keys
    re.compile(r'COHERE_API_KEY\s*=\s*[\'"]([^\'"]+)[\'"]'),  # COHERE_API_KEY assignments
]

# Function to search GitHub for potential API keys
def search_github(query, page=1):
    url = "https://api.github.com/search/code"
    params = {"q": query, "per_page": 10 if TEST_MODE else 30, "page": page}
    
    try:
        if VERBOSE_LOGGING:
            print(f"Searching GitHub with query: {query} (page {page})")
            
        response = requests.get(url, headers=HEADERS, params=params)
        
        if response.status_code == 200:
            result = response.json()
            if VERBOSE_LOGGING:
                print(f"Found {len(result.get('items', []))} results")
            return result
        elif response.status_code == 403:
            rate_limit = int(response.headers.get('X-RateLimit-Reset', 0)) - int(time.time())
            wait_time = max(rate_limit, 60)
            print(f"⚠️ Rate limit exceeded. Waiting {wait_time} seconds...")
            time.sleep(wait_time)
            return search_github(query, page)
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Exception during GitHub search: {str(e)}")
        time.sleep(10)
        return None

# Function to extract API keys from a file
def extract_keys_from_file(file_url, repo_name, file_path):
    try:
        if VERBOSE_LOGGING:
            print(f"Fetching file content from: {file_url}")
            
        raw_response = requests.get(file_url)
        if raw_response.status_code == 200:
            content = raw_response.text
            extracted_keys = []
            
            for pattern in LLM_KEY_PATTERNS:
                matches = pattern.findall(content)
                for match in matches:
                    # If the pattern captured a group, use the group value
                    # Otherwise use the whole match
                    key = match[0] if isinstance(match, tuple) else match
                    
                    # Determine key type based on format or variable name
                    if key.startswith("sk-") and len(key) >= 48:
                        key_type = "OpenAI API"
                    elif key.startswith("AIza"):
                        key_type = "Google Gemini/PaLM API"
                    elif key.startswith("sk-ant-"):
                        key_type = "Anthropic API"
                    elif "OPENAI" in content:
                        key_type = "OpenAI API"
                    elif "GEMINI" in content or "PALM" in content or "GOOGLE_API" in content:
                        key_type = "Google Gemini/PaLM API"
                    elif "ANTHROPIC" in content:
                        key_type = "Anthropic API"
                    elif "COHERE" in content:
                        key_type = "Cohere API"
                    else:
                        key_type = "Unknown LLM API"
                    
                    # Get surrounding context (up to 50 chars before and after)
                    key_pos = content.find(key)
                    start_pos = max(0, key_pos - 50)
                    end_pos = min(len(content), key_pos + len(key) + 50)
                    context = content[start_pos:end_pos].replace(key, "[REDACTED]")
                    
                    if VERBOSE_LOGGING:
                        print(f"Found {key_type} key: {key[:4]}...{key[-4:] if len(key) > 8 else ''}")
                    
                    # Only add if not already in the list and key has minimum viable length
                    if len(key) >= 20 and not any(k["key"] == key for k in extracted_keys):
                        extracted_keys.append({
                            "key": key,
                            "type": key_type,
                            "context": context
                        })
            
            return extracted_keys if extracted_keys else None
        else:
            print(f"❌ Failed to fetch file: {raw_response.status_code}")
            
    except Exception as e:
        print(f"❌ Error extracting keys from {repo_name}/{file_path}: {str(e)}")
    
    return None

# Function to test OpenAI API key validity
def test_openai_api_key(api_key):
    try:
        if VERBOSE_LOGGING:
            print(f"Testing OpenAI API key: {api_key[:4]}...{api_key[-4:] if len(api_key) > 8 else ''}")
            
        url = "https://api.openai.com/v1/models"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.get(url, headers=headers)
        is_valid = response.status_code == 200
        
        if VERBOSE_LOGGING:
            print(f"OpenAI API key is {'valid' if is_valid else 'invalid'} (status code: {response.status_code})")
            
        return is_valid
    except Exception as e:
        if VERBOSE_LOGGING:
            print(f"Error testing OpenAI API key: {str(e)}")
        return False

# Function to test Google Gemini API key validity
def test_gemini_api_key(api_key):
    try:
        if VERBOSE_LOGGING:
            print(f"Testing Google Gemini API key: {api_key[:4]}...{api_key[-4:] if len(api_key) > 8 else ''}")
            
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={api_key}"
        payload = {"contents": [{"parts": [{"text": "Hello"}]}]}
        headers = {"Content-Type": "application/json"}

        response = requests.post(url, json=payload, headers=headers)
        is_valid = response.status_code == 200
        
        if VERBOSE_LOGGING:
            print(f"Google API key is {'valid' if is_valid else 'invalid'} (status code: {response.status_code})")
            
        return is_valid
    except Exception as e:
        if VERBOSE_LOGGING:
            print(f"Error testing Google API key: {str(e)}")
        return False

# Function to test Anthropic API key validity
def test_anthropic_api_key(api_key):
    try:
        if VERBOSE_LOGGING:
            print(f"Testing Anthropic API key: {api_key[:4]}...{api_key[-4:] if len(api_key) > 8 else ''}")
            
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        
        payload = {
            "model": "claude-3-opus-20240229",
            "max_tokens": 1,
            "messages": [{"role": "user", "content": "Hello"}]
        }
        
        response = requests.post(url, json=payload, headers=headers)
        is_valid = response.status_code in [200, 201]
        
        if VERBOSE_LOGGING:
            print(f"Anthropic API key is {'valid' if is_valid else 'invalid'} (status code: {response.status_code})")
            
        return is_valid
    except Exception as e:
        if VERBOSE_LOGGING:
            print(f"Error testing Anthropic API key: {str(e)}")
        return False

# Function to test Cohere API key validity
def test_cohere_api_key(api_key):
    try:
        if VERBOSE_LOGGING:
            print(f"Testing Cohere API key: {api_key[:4]}...{api_key[-4:] if len(api_key) > 8 else ''}")
            
        url = "https://api.cohere.ai/v1/generate"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "prompt": "Hello",
            "max_tokens": 1
        }
        
        response = requests.post(url, json=payload, headers=headers)
        is_valid = response.status_code == 200
        
        if VERBOSE_LOGGING:
            print(f"Cohere API key is {'valid' if is_valid else 'invalid'} (status code: {response.status_code})")
            
        return is_valid
    except Exception as e:
        if VERBOSE_LOGGING:
            print(f"Error testing Cohere API key: {str(e)}")
        return False

# Function to notify repository owner via GitHub issue
def create_github_issue(repo, file_path, key_info):
    if DRY_RUN:
        print(f"🔸 [DRY RUN] Would create issue in {repo} for exposed {key_info['type']} key")
        return True
        
    try:
        # Check if we have permission to create an issue
        check_url = f"https://api.github.com/repos/{repo}"
        check_response = requests.get(check_url, headers=HEADERS)
        
        if check_response.status_code != 200:
            print(f"❌ Cannot access repository {repo}. Skipping issue creation.")
            return False
            
        url = f"https://api.github.com/repos/{repo}/issues"
        issue_title = "⚠️ Security Alert: LLM API Key Exposed!"
        
        # Create a redacted version of the key for the issue
        key_type = key_info["type"]
        key = key_info["key"]
        redacted_key = key[:4] + "..." + (key[-4:] if len(key) > 8 else "")
        
        issue_body = (
            f"Hello,\n\n"
            f"It looks like your repository contains an **exposed {key_type} key** in the file `{file_path}`.\n\n"
            f"The key beginning with `{redacted_key}` appears to be a valid API key.\n\n"
            f"### 🔴 Why is this a problem?\n"
            f"- Exposed API keys can be exploited by malicious users\n"
            f"- Your account might be charged for unauthorized API usage\n"
            f"- These keys can be used for prompt injection, data extraction, or other malicious activities\n\n"
            f"### ✅ What should you do?\n"
            f"1. **Immediately revoke the key** and generate a new one\n"
            f"2. **Remove the exposed key from your repository** (including commit history if necessary)\n"
            f"3. **Use environment variables or secrets** to store API keys securely\n\n"
            f"This notification was sent by KeySamaritan, "
            f"an automated tool that helps detect exposed API keys in public repositories.\n\n"
            f"Stay safe! 🚀"
        )

        payload = {"title": issue_title, "body": issue_body}
        response = requests.post(url, headers=HEADERS, json=payload)

        if response.status_code == 201:
            print(f"✅ Issue successfully created in {repo}!")
            return True
        else:
            print(f"❌ Failed to create issue in {repo}: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error creating issue for {repo}: {str(e)}")
        return False

# Function to generate a markdown report of findings
def generate_report(findings):
    report = f"# LLM API Key Findings Report\n\n"
    report += f"Scan Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report += f"## Summary\n\n"
    report += f"- Total repositories scanned: {findings['stats']['total_repos']}\n"
    report += f"- Repositories with LLM API keys: {len(findings['repos'])}\n"
    report += f"- Total LLM API keys found: {findings['stats']['total_keys']}\n"
    report += f"- Valid LLM API keys: {findings['stats']['valid_keys']}\n"
    report += f"- Invalid LLM API keys: {findings['stats']['invalid_keys']}\n\n"
    
    if TEST_MODE:
        report += f"**Note:** This report was generated in test mode.\n\n"
    
    # Break down by key type
    key_types = {}
    for repo_name, repo_data in findings['repos'].items():
        for file_info in repo_data['files']:
            for key_info in file_info['keys']:
                key_type = key_info['type']
                if key_type not in key_types:
                    key_types[key_type] = {"total": 0, "valid": 0}
                key_types[key_type]["total"] += 1
                if key_info['valid']:
                    key_types[key_type]["valid"] += 1
    
    report += "## Key Types Found\n\n"
    for key_type, counts in key_types.items():
        report += f"- {key_type}: {counts['total']} total, {counts['valid']} valid\n"
    
    report += f"\n## Detailed Findings\n\n"
    
    for repo_name, repo_data in findings['repos'].items():
        report += f"### {repo_name}\n\n"
        
        for file_info in repo_data['files']:
            report += f"**File:** {file_info['path']}\n\n"
            
            for key_info in file_info['keys']:
                status = "✅ Valid" if key_info['valid'] else "❌ Invalid"
                key = key_info['key']
                report += f"- [{status}] {key_info['type']} key (redacted: {key[:4]}...{key[-4:] if len(key) > 8 else ''})\n"
                report += f"  - Context: `{key_info['context']}`\n"
                
                if key_info['notified']:
                    report += f"  - ✉️ Repository owner notified\n"
                else:
                    report += f"  - ❓ Could not notify repository owner\n"
            
            report += "\n"
    
    return report

# Main function
def main():
    if TEST_MODE:
        print("🧪 Running LLM Key Scanner in TEST MODE")
        print(f"- Maximum repositories to check: {MAX_REPOS_TO_CHECK}")
        print(f"- Dry run (no actual issues created): {DRY_RUN}")
        print(f"- Verbose logging: {VERBOSE_LOGGING}")
        print("=" * 50)
    
    # More focused queries for LLM API keys
    queries = [
        '"OPENAI_API_KEY"',
        '"openai.api_key"',
        '"sk-" extension:py',
        '"sk-" extension:js',
        '"sk-" extension:env',
        '"AIza" extension:py',
        '"AIza" extension:js',
        '"AIza" extension:env',
        '"GEMINI_API_KEY"', 
        '"GOOGLE_API_KEY"',
        '"ANTHROPIC_API_KEY"',
        '"COHERE_API_KEY"',
        'filename:.env "OPENAI"',
        'filename:.env "GEMINI"',
        'filename:.env "ANTHROPIC"',
        'filename:.env "COHERE"',
        'filename:config "openai"',
        'filename:credentials "openai"'
    ]
    
    findings = {
        "stats": {
            "total_repos": 0,
            "total_keys": 0,
            "valid_keys": 0,
            "invalid_keys": 0
        },
        "repos": {}
    }
    
    valid_keys = set()
    invalid_keys = set()
    
    print(f"🔍 Starting LLM API Key scan...")
    
    for query in queries:
        print(f"🔎 Searching GitHub for: {query}")
        page = 1
        repos_checked = 0
        
        while repos_checked < MAX_REPOS_TO_CHECK:
            result = search_github(query, page)
            
            if not result or "items" not in result or len(result["items"]) == 0:
                print(f"No more results found for query: {query}")
                break
                
            for item in result["items"]:
                repo_name = item["repository"]["full_name"]
                file_path = item["path"]
                raw_url = item["html_url"].replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
                
                # Skip repositories we've already processed
                if repo_name in findings["repos"] and any(file_info["path"] == file_path for file_info in findings["repos"][repo_name]["files"]):
                    if VERBOSE_LOGGING:
                        print(f"📋 Already processed {repo_name}/{file_path}, skipping")
                    continue
                    
                print(f"📂 Checking {repo_name}/{file_path}...")
                findings["stats"]["total_repos"] += 1
                repos_checked += 1
                
                keys = extract_keys_from_file(raw_url, repo_name, file_path)
                
                if keys:
                    print(f"🔑 Found {len(keys)} potential LLM API keys in {repo_name}/{file_path}")
                    
                    # Initialize repo entry if it doesn't exist
                    if repo_name not in findings["repos"]:
                        findings["repos"][repo_name] = {"files": []}
                        
                    file_info = {"path": file_path, "keys": []}
                    
                    for key_data in keys:
                        key = key_data["key"]
                        key_type = key_data["type"]
                        context = key_data["context"]
                        
                        print(f"🔑 Found {key_type} key in {repo_name}/{file_path}")
                        findings["stats"]["total_keys"] += 1
                        
                        # Test key validity based on key type
                        is_valid = False
                        if key_type == "OpenAI API":
                            is_valid = test_openai_api_key(key)
                        elif key_type == "Google Gemini/PaLM API":
                            is_valid = test_gemini_api_key(key)
                        elif key_type == "Anthropic API":
                            is_valid = test_anthropic_api_key(key)
                        elif key_type == "Cohere API":
                            is_valid = test_cohere_api_key(key)
                        
                        # Record key validity
                        if is_valid:
                            print(f"✅ Valid {key_type} key found")
                            valid_keys.add(key)
                            findings["stats"]["valid_keys"] += 1
                        else:
                            print(f"❌ Invalid {key_type} key")
                            invalid_keys.add(key)
                            findings["stats"]["invalid_keys"] += 1
                        
                        # Only notify for valid keys
                        notified = False
                        if is_valid:
                            notified = create_github_issue(repo_name, file_path, key_data)
                        
                        # Add key to file info
                        file_info["keys"].append({
                            "key": key,
                            "type": key_type,
                            "valid": is_valid,
                            "notified": notified,
                            "context": context
                        })
                    
                    # Add file info to repo
                    findings["repos"][repo_name]["files"].append(file_info)
                
                if repos_checked >= MAX_REPOS_TO_CHECK:
                    break
                    
                # Respect GitHub rate limits
                time.sleep(2 if TEST_MODE else 1)
            
            page += 1
    
    # Save valid and invalid keys to files
    with open(VALID_KEYS_FILE, "w") as valid_file:
        for key in valid_keys:
            # Save only the first 4 and last 4 characters for security
            valid_file.write(f"{key[:4]}...{key[-4:] if len(key) > 8 else ''}\n")

    with open(INVALID_KEYS_FILE, "w") as invalid_file:
        for key in invalid_keys:
            # Save only the first 4 and last 4 characters for security
            invalid_file.write(f"{key[:4]}...{key[-4:] if len(key) > 8 else ''}\n")
    
    # Generate and save report
    report = generate_report(findings)
    with open(FINDINGS_REPORT, "w") as report_file:
        report_file.write(report)
    
    print(f"\n✅ Scan complete!")
    print(f"- Total repositories scanned: {findings['stats']['total_repos']}")
    print(f"- Repositories with exposed keys: {len(findings['repos'])}")
    print(f"- Valid keys found: {findings['stats']['valid_keys']}")
    print(f"- Invalid keys found: {findings['stats']['invalid_keys']}")
    print(f"- Results saved to {FINDINGS_REPORT}")

if __name__ == "__main__":
    main()