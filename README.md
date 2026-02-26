<p align="center">
  <img src="https://github.com/kirk-haodong/wechat-mp-fetcher/blob/master/assets/logo.png?raw=true" alt="WeChat MP Fetcher" width="180">
</p>

<h1 align="center">WeChat MP Fetcher</h1>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+"></a>
  <a href="https://github.com/kirk-haodong/wechat-mp-fetcher/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License"></a>
  <a href="https://github.com/kirk-haodong/wechat-mp-fetcher/stargazers"><img src="https://img.shields.io/github/stars/kirk-haodong/wechat-mp-fetcher.svg?style=social" alt="GitHub stars"></a>
</p>

<p align="center">
  <a href="README.md">English</a> •
  <a href="README.zh.md">中文</a> •
  <a href="README.ja.md">日本語</a>
</p>

<p align="center">
  A powerful tool for fetching articles from WeChat Official Accounts
</p>

---

## ✨ Features

- 🐳 **One-click Docker deployment** of we-mp-rss service
- 📱 **QR code login** to WeChat MP Platform
- 🔍 **Smart search** and add official accounts
- 📄 **Automatic article fetching** with pagination support
- 📊 **Article statistics** and management
- 🔧 **Built-in troubleshooting** tools

## 🚀 Quick Start

### Prerequisites

- Docker 20.10+
- Python 3.8+
- Port 4000 available

### 1. Deploy Service

```bash
bash scripts/deploy.sh
```

### 2. Login to WeChat MP Platform

```bash
python3 scripts/login.py
```

> ⚠️ **Important**: You must select **"Official Account"** login method (not Mini Program)!

### 3. Add Official Accounts

```bash
python3 scripts/add_mp.py "Account Name"

# Examples
python3 scripts/add_mp.py "新智元"
python3 scripts/add_mp.py "量子位"
```

### 4. Fetch Articles

```bash
# Fetch all accounts
python3 scripts/fetch_articles.py --all

# Fetch specific account
python3 scripts/fetch_articles.py --mp "Account Name"

# Specify page count
python3 scripts/fetch_articles.py --mp "Account Name" --pages 2
```

### 5. View Statistics

```bash
python3 scripts/show_stats.py
```

## 📁 Project Structure

```
wechat-mp-fetcher/
├── README.md              # This file
├── README.zh.md           # 中文文档
├── README.ja.md           # 日本語ドキュメント
├── SKILL.md               # Detailed guide with troubleshooting
├── scripts/               # Scripts
│   ├── deploy.sh          # Deployment script
│   ├── login.py           # Login (QR code + wait)
│   ├── get_token.py       # Get API token
│   ├── add_mp.py          # Add official account
│   ├── fetch_articles.py  # Fetch articles
│   ├── show_stats.py      # Show statistics
│   └── fix_issues.py      # Troubleshooting tool
├── data/                  # Data directory
│   └── db.db              # SQLite database
└── assets/                # Assets
    ├── logo.png           # Logo (PNG)
    └── logo.svg           # Logo (SVG)
```

## 🛠️ Troubleshooting

### Cannot search after login (200002 error)

**Cause**: Wrong login method (e.g., Mini Program instead of Official Account)

**Solution**:
```bash
python3 scripts/fix_issues.py
```

Then re-login and select **"Official Account"** method.

### Docker image pull fails

The deploy script will automatically prompt for solutions:
1. Configure Docker domestic mirror
2. Use proxy
3. Manual download

See [SKILL.md](SKILL.md) for detailed troubleshooting.

## 📄 License

[MIT](LICENSE) © kirk-haodong

## 🙏 Acknowledgments

- [we-mp-rss](https://github.com/rachelos/we-mp-rss) project for core functionality
