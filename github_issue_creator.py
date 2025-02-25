import requests
import re
import time
import openai  # OpenAI library for API key testing
import os

# Your GitHub Token (Ensure it has `public_repo` permission)
GITHUB_TOKEN = os.environ["GH_TOKEN"]  # Insert your GitHub personal access token here

# Headers for GitHub API requests
HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {GITHUB_TOKEN}" if GITHUB_TOKEN else None,
}

# Regex patterns to detect API keys
API_KEY_PATTERNS = [
    re.compile(r'API_KEY\s*=\s*"([A-Za-z0-9-_]{6,})"'),  # Generic API Keys
    re.compile(r'AIza[0-9A-Za-z-_]{35}'),  # Google Gemini API Keys
    re.compile(r'sk-[A-Za-z0-9]{48}'),  # OpenAI API Keys (Starts with 'sk-')
]

# Output files
VALID_KEYS_FILE = "valid_api_keys.txt"
INVALID_KEYS_FILE = "invalid_api_keys.txt"

# Maximum number of warnings (for testing)
MAX_WARNINGS = 2


# Function to search GitHub for potential API keys
def search_github(query, page=1):
    url = "https://api.github.com/search/code"
    params = {"q": query, "per_page": 10, "page": page}  # Reduced per_page for testing
    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 403:
        print("Rate limit exceeded. Waiting 60 seconds...")
        time.sleep(60)
        return search_github(query, page)
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


# Function to extract API keys from a file
def extract_keys_from_file(file_url):
    raw_response = requests.get(file_url)
    if raw_response.status_code == 200:
        content = raw_response.text
        extracted_keys = set()
        for pattern in API_KEY_PATTERNS:
            keys = pattern.findall(content)
            extracted_keys.update(keys)
        return extracted_keys if extracted_keys else None
    return None


# Function to test Google Gemini API key validity
def test_gemini_api_key(api_key):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={api_key}"
    payload = {"contents": [{"parts": [{"text": "Hello"}]}]}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    return response.status_code == 200  # Returns True if valid


# Function to test OpenAI API key validity
def test_openai_api_key(api_key):
    try:
        client = openai.OpenAI(api_key=api_key)
        client.models.list()
        return True  # API key is valid
    except openai.AuthenticationError:
        return False  # API key is invalid


# Function to save API keys to files
def save_keys_to_file(valid_keys, invalid_keys):
    with open(VALID_KEYS_FILE, "w") as valid_file:
        for key in valid_keys:
            valid_file.write(key + "\n")

    with open(INVALID_KEYS_FILE, "w") as invalid_file:
        for key in invalid_keys:
            invalid_file.write(key + "\n")

    print(f"✅ Valid keys saved to {VALID_KEYS_FILE}")
    print(f"❌ Invalid keys saved to {INVALID_KEYS_FILE}")


# Function to create a GitHub issue warning the repository owner
def create_github_issue(repo, file_path):
    url = f"https://api.github.com/repos/{repo}/issues"
    issue_title = "⚠️ Security Warning: API Key Exposed!"
    issue_body = (
        f"Hello,\n\n"
        f"It looks like your repository `{repo}` contains an **exposed API key** in the file `{file_path}`.\n\n"
        f"### 🔴 Why is this a problem?\n"
        f"- Exposed API keys can be exploited by malicious users.\n"
        f"- Your account might be charged for unauthorized API usage.\n"
        f"- Some services may automatically revoke your key if it is publicly exposed.\n\n"
        f"### ✅ What should you do?\n"
        f"1. **Immediately revoke the key** and generate a new one.\n"
        f"2. **Remove the exposed key from your repository** (including commit history if necessary).\n"
        f"3. **Use environment variables or secrets** to store API keys securely instead of hardcoding them.\n\n"
        f"To learn more about securing your API keys, check out GitHub’s [security best practices](https://docs.github.com/en/code-security).\n\n"
        f"Stay safe! 🚀"
    )

    payload = {"title": issue_title, "body": issue_body}
    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code == 201:
        print(f"Issue successfully created in {repo}!")
    else:
        print(f"Failed to create issue in {repo}: {response.text}")


# Main function to search, extract, test, and warn
def main():
    query = '"API_KEY"'
    page = 1
    warned_repos = set()
    valid_keys = set()
    invalid_keys = set()

    print(f"🔍 Searching GitHub for repositories with exposed API keys (Testing on {MAX_WARNINGS} repos)...")

    while len(warned_repos) < MAX_WARNINGS:
        result = search_github(query, page)
        if not result or "items" not in result or len(result["items"]) == 0:
            print("No more results found.")
            break

        for item in result["items"]:
            repo_name = item["repository"]["full_name"]
            file_path = item["path"]
            raw_url = item["html_url"].replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")

            if repo_name in warned_repos:
                continue

            print(f"📂 Checking {repo_name}/{file_path}...")

            keys = extract_keys_from_file(raw_url)
            if keys:
                print(f"🔑 Found API keys in {repo_name}/{file_path}: {keys}")

                for key in keys:
                    if key.startswith("AIza"):  # Google Gemini API Key
                        if test_gemini_api_key(key):
                            print(f"✅ Valid Google Gemini API key: {key}")
                            valid_keys.add(key)
                        else:
                            print(f"❌ Invalid Google Gemini API key: {key}")
                            invalid_keys.add(key)
                    elif key.startswith("sk-"):  # OpenAI API Key
                        if test_openai_api_key(key):
                            print(f"✅ Valid OpenAI API key: {key}")
                            valid_keys.add(key)
                        else:
                            print(f"❌ Invalid OpenAI API key: {key}")
                            invalid_keys.add(key)
                    else:  # Unknown key format (considering valid)
                        print(f"⚠️ Unknown API key format: {key}")
                        valid_keys.add(key)

                create_github_issue(repo_name, file_path)
                warned_repos.add(repo_name)

            if len(warned_repos) >= MAX_WARNINGS:
                break

        page += 1
        time.sleep(1)

    save_keys_to_file(valid_keys, invalid_keys)
    print(f"\n🚀 Warnings sent to {len(warned_repos)} repositories.")

if __name__ == "__main__":
    main()