# WeChat MP Fetcher

<p align="center">
  <img src="https://github.com/kirk-haodong/wechat-mp-fetcher/blob/master/assets/logo.png?raw=true" alt="WeChat MP Fetcher Logo" width="120">
</p>

<p align="center">
  <a href="#english">English</a> | 
  <a href="#中文">中文</a> | 
  <a href="#日本語">日本語
</p>

---

<h2 id="english">🇺🇸 English</h2>

A powerful tool for fetching articles from WeChat Official Accounts. Deploy we-mp-rss service via Docker, login to WeChat MP Platform, and automatically fetch articles from specified accounts.

## Features

- 🐳 One-click Docker deployment of we-mp-rss service
- 📱 QR code login to WeChat MP Platform
- 🔍 Smart search and add official accounts
- 📄 Automatic article fetching
- 📊 Article statistics and management
- 🔧 Built-in troubleshooting tools

## Quick Start

### 1. Deploy Service

```bash
bash scripts/deploy.sh
```

### 2. Login to WeChat MP Platform

```bash
python3 scripts/login.py
```

**⚠️ Important**: You must select **"Official Account"** login method (not Mini Program)!

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

## Troubleshooting

### Cannot search after login (200002 error)

**Cause**: Wrong login method (e.g., Mini Program instead of Official Account)

**Solution**: Re-login and select **"Official Account"** method

```bash
python3 scripts/fix_issues.py
```

### Docker image pull fails

The deploy script will automatically prompt for solutions:
1. Configure Docker domestic mirror
2. Use proxy
3. Manual download

See [SKILL.md](SKILL.md) for detailed troubleshooting.

---

<h2 id="中文">🇨🇳 中文</h2>

微信公众号文章抓取工具 - 通过 Docker 部署 we-mp-rss 服务，实现微信公众号文章的自动抓取。

## 功能特性

- 🐳 Docker 一键部署 we-mp-rss 服务
- 📱 微信公众号平台扫码登录
- 🔍 智能搜索并添加公众号
- 📄 自动抓取文章内容
- 📊 文章统计与管理
- 🔧 内置故障排除工具

## 快速开始

### 1. 部署服务

```bash
bash scripts/deploy.sh
```

### 2. 登录微信公众号平台

```bash
python3 scripts/login.py
```

**⚠️ 重要**：必须使用**公众号**登录方式（不是小程序）！

### 3. 添加公众号

```bash
python3 scripts/add_mp.py "公众号名称"

# 示例
python3 scripts/add_mp.py "新智元"
python3 scripts/add_mp.py "量子位"
```

### 4. 抓取文章

```bash
# 抓取所有公众号
python3 scripts/fetch_articles.py --all

# 抓取指定公众号
python3 scripts/fetch_articles.py --mp "公众号名称"

# 指定抓取页数
python3 scripts/fetch_articles.py --mp "公众号名称" --pages 2
```

### 5. 查看统计

```bash
python3 scripts/show_stats.py
```

## 故障排除

### 登录后无法搜索（200002 错误）

**原因**：使用了错误的登录方式（如小程序而不是公众号）

**解决**：重新登录并选择**公众号**方式

```bash
python3 scripts/fix_issues.py
```

### Docker 镜像拉取失败

部署脚本会自动提示解决方案：
1. 配置 Docker 国内镜像源
2. 使用代理
3. 手动下载

详细故障排除请参阅 [SKILL.md](SKILL.md)。

---

<h2 id="日本語">🇯🇵 日本語</h2>

WeChat 公式アカウント記事取得ツール - Docker で we-mp-rss サービスをデプロイし、WeChat 公式プラットフォームにログインして、指定したアカウントの記事を自動的に取得します。

## 機能

- 🐳 Docker ワンクリックデプロイ
- 📱 WeChat 公式プラットフォーム QR ログイン
- 🔍 スマート検索とアカウント追加
- 📄 自動記事取得
- 📊 記事統計と管理
- 🔧 内蔵トラブルシューティングツール

## クイックスタート

### 1. サービスをデプロイ

```bash
bash scripts/deploy.sh
```

### 2. WeChat 公式プラットフォームにログイン

```bash
python3 scripts/login.py
```

**⚠️ 重要**：**公式アカウント**ログイン方式を選択してください（ミニプログラムではありません）！

### 3. 公式アカウントを追加

```bash
python3 scripts/add_mp.py "アカウント名"

# 例
python3 scripts/add_mp.py "新智元"
python3 scripts/add_mp.py "量子位"
```

### 4. 記事を取得

```bash
# すべてのアカウント
python3 scripts/fetch_articles.py --all

# 特定のアカウント
python3 scripts/fetch_articles.py --mp "アカウント名"

# ページ数を指定
python3 scripts/fetch_articles.py --mp "アカウント名" --pages 2
```

### 5. 統計を表示

```bash
python3 scripts/show_stats.py
```

## トラブルシューティング

### ログイン後に検索できない（200002 エラー）

**原因**：ログイン方式が間違っている（ミニプログラムなど）

**解決**：**公式アカウント**方式で再ログイン

```bash
python3 scripts/fix_issues.py
```

### Docker イメージ取得失敗

デプロイスクリプトが自動的に解決策を提示します：
1. Docker 国内ミラーを設定
2. プロキシを使用
3. 手動ダウンロード

詳細は [SKILL.md](SKILL.md) を参照してください。

---

## System Requirements / 系统要求 / システム要件

- Docker 20.10+
- Python 3.8+
- Port 4000 available / 开放 4000 端口 / ポート 4000 が利用可能

## Installation / 安装 / インストール

```bash
pip install requests
```

## Project Structure / 项目结构 / プロジェクト構造

```
wechat-mp-fetcher/
├── README.md              # This file
├── SKILL.md               # Detailed guide (with troubleshooting)
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
    ├── logo.png           # Logo
    └── logo.svg           # Logo (SVG)
```

## Tech Stack / 技术栈 / 技術スタック

- [we-mp-rss](https://github.com/rachelos/we-mp-rss) - WeChat MP RSS service
- Docker - Container deployment
- SQLite - Data storage
- Python - Scripting

## License / 许可证 / ライセンス

MIT License

## Contributing / 贡献 / 貢献

Issues and Pull Requests are welcome! / 欢迎提交 Issue 和 Pull Request！ / Issue と Pull Request を歓迎します！

## Acknowledgments / 致谢 / 謝辞

- [we-mp-rss](https://github.com/rachelos/we-mp-rss) project for core functionality
