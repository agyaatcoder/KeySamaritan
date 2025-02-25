# KeySamaritan 🔑

KeySamaritan is an automated tool that scans GitHub repositories for exposed API keys, tests their validity, and notifies repository owners about potential security risks.


## 🌟 Features

- **Automated Scanning**: Search GitHub for exposed API keys in public repositories
- **Validity Testing**: Test discovered keys to confirm they're active before notifying
- **Owner Notification**: Create GitHub issues to alert repository owners about exposed keys
- **Comprehensive Reporting**: Generate detailed reports of findings
- **Multiple Key Types**: Detects several types of API keys:
  - OpenAI API Keys
  - Google Gemini API Keys
  - GitHub Personal Access Tokens
  - AWS Access Keys
  - Generic API Keys

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- GitHub Personal Access Token with `public_repo` scope

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/keysamaritan.git
   cd keysamaritan
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your GitHub token:
   ```bash
   export GITHUB_TOKEN=your_github_token
   ```

### Running Manually

```bash
python keysamaritan.py
```

### Setting Up as a GitHub Action

1. Fork this repository
2. Add your GitHub token as a repository secret named `GITHUB_TOKEN`
3. The action will run automatically according to the schedule in the workflow file

## 📊 Reports

KeySamaritan generates several output files:

- `findings_report.md`: Detailed markdown report of all findings
- `valid_api_keys.txt`: List of valid API keys (redacted for security)
- `invalid_api_keys.txt`: List of invalid API keys

## 🛠 Customization

You can customize KeySamaritan by modifying these variables in the script:

- `MAX_REPOS_TO_CHECK`: Maximum number of repositories to check per run
- `API_KEY_PATTERNS`: Regular expressions for detecting different types of API keys

## 🔒 Security Considerations

KeySamaritan is designed to help improve security across GitHub repositories. However, please use it responsibly:

- **Never use discovered API keys** - Report them to their owners
- **Don't store valid API keys** - The tool redacts keys in reports
- **Be respectful of rate limits** - The tool includes rate limiting logic

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📬 Contact

If you have any questions or feedback, please open an issue or contact [your-email@example.com](mailto:your-email@example.com).

---

Created with ❤️ to make GitHub a more secure place.