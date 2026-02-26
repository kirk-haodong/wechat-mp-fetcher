<p align="center">
  <img src="https://github.com/kirk-haodong/wechat-mp-fetcher/blob/master/assets/logo.png?raw=true" alt="WeChat MP Fetcher" width="180">
</p>

<h1 align="center">微信公众号文章抓取工具</h1>

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
  通过 Docker 部署 we-mp-rss 服务，实现微信公众号文章的自动抓取
</p>

---

## ✨ 功能特性

- 🐳 **Docker 一键部署** we-mp-rss 服务
- 📱 **微信公众号平台** 扫码登录
- 🔍 **智能搜索** 并添加公众号
- 📄 **自动抓取文章** 支持分页
- 📊 **文章统计** 与管理
- 🔧 **内置故障排除** 工具

## 🚀 快速开始

### 前置要求

- Docker 20.10+
- Python 3.8+
- 开放端口 4000

### 1. 部署服务

```bash
bash scripts/deploy.sh
```

### 2. 登录微信公众号平台

```bash
python3 scripts/login.py
```

> ⚠️ **重要**：必须使用**公众号**登录方式（不是小程序）！

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

## 📁 项目结构

```
wechat-mp-fetcher/
├── README.md              # 英文文档
├── README.zh.md           # 本文档
├── README.ja.md           # 日本語ドキュメント
├── SKILL.md               # 详细使用指南（含故障排除）
├── scripts/               # 脚本目录
│   ├── deploy.sh          # 部署脚本
│   ├── login.py           # 登录脚本（二维码+等待）
│   ├── get_token.py       # 获取 API Token
│   ├── add_mp.py          # 添加公众号
│   ├── fetch_articles.py  # 抓取文章
│   ├── show_stats.py      # 显示统计
│   └── fix_issues.py      # 故障排除工具
├── data/                  # 数据目录
│   └── db.db              # SQLite 数据库
└── assets/                # 资源文件
    ├── logo.png           # Logo (PNG)
    └── logo.svg           # Logo (SVG)
```

## 🛠️ 故障排除

### 登录后无法搜索（200002 错误）

**原因**：使用了错误的登录方式（如小程序而不是公众号）

**解决方案**：
```bash
python3 scripts/fix_issues.py
```

然后重新登录并选择**公众号**方式。

### Docker 镜像拉取失败

部署脚本会自动提示解决方案：
1. 配置 Docker 国内镜像源
2. 使用代理
3. 手动下载

详细故障排除请参阅 [SKILL.md](SKILL.md)。

## 📄 许可证

[MIT](LICENSE) © kirk-haodong

## 🙏 致谢

- [we-mp-rss](https://github.com/rachelos/we-mp-rss) 项目提供核心功能
