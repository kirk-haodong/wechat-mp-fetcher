<p align="center">
  <img src="https://github.com/kirk-haodong/wechat-mp-fetcher/blob/master/assets/logo.png?raw=true" alt="WeChat MP Fetcher" width="180">
</p>

<h1 align="center">WeChat 公式アカウント記事取得ツール</h1>

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
  Docker で we-mp-rss サービスをデプロイし、WeChat 公式アカウントの記事を自動的に取得
</p>

---

## ✨ 機能

- 🐳 **Docker ワンクリックデプロイ** we-mp-rss サービス
- 📱 **WeChat 公式プラットフォーム** QR コードログイン
- 🔍 **スマート検索** でアカウント追加
- 📄 **自動記事取得** ページネーション対応
- 📊 **記事統計** と管理
- 🔧 **内蔵トラブルシューティング** ツール

## 🚀 クイックスタート

### 前提条件

- Docker 20.10+
- Python 3.8+
- ポート 4000 が利用可能

### 1. サービスをデプロイ

```bash
bash scripts/deploy.sh
```

### 2. WeChat 公式プラットフォームにログイン

```bash
python3 scripts/login.py
```

> ⚠️ **重要**：**公式アカウント**ログイン方式を選択してください（ミニプログラムではありません）！

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

## 📁 プロジェクト構造

```
wechat-mp-fetcher/
├── README.md              # 英文ドキュメント
├── README.zh.md           # 中文ドキュメント
├── README.ja.md           # 本ドキュメント
├── SKILL.md               # 詳細ガイド（トラブルシューティング含む）
├── scripts/               # スクリプト
│   ├── deploy.sh          # デプロイスクリプト
│   ├── login.py           # ログイン（QRコード+待機）
│   ├── get_token.py       # API Token 取得
│   ├── add_mp.py          # アカウント追加
│   ├── fetch_articles.py  # 記事取得
│   ├── show_stats.py      # 統計表示
│   └── fix_issues.py      # トラブルシューティング
├── data/                  # データディレクトリ
│   └── db.db              # SQLite データベース
└── assets/                # アセット
    ├── logo.png           # Logo (PNG)
    └── logo.svg           # Logo (SVG)
```

## 🛠️ トラブルシューティング

### ログイン後に検索できない（200002 エラー）

**原因**：ログイン方式が間違っている（ミニプログラムなど）

**解決方法**：
```bash
python3 scripts/fix_issues.py
```

その後、**公式アカウント**方式で再ログインしてください。

### Docker イメージ取得失敗

デプロイスクリプトが自動的に解決策を提示します：
1. Docker 国内ミラーを設定
2. プロキシを使用
3. 手動ダウンロード

詳細は [SKILL.md](SKILL.md) を参照してください。

## 📄 ライセンス

[MIT](LICENSE) © kirk-haodong

## 🙏 謝辞

- [we-mp-rss](https://github.com/rachelos/we-mp-rss) プロジェクトがコア機能を提供
