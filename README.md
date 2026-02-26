# WeChat MP Fetcher

微信公众号文章抓取工具 - 通过 Docker 部署 we-mp-rss 服务，实现微信公众号文章的自动抓取。

## 功能特性

- 🐳 Docker 一键部署 we-mp-rss 服务
- 📱 微信公众号平台扫码登录
- 🔍 智能搜索并添加公众号
- 📄 自动抓取文章内容
- 📊 文章统计与管理

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/wechat-mp-fetcher.git
cd wechat-mp-fetcher
```

### 2. 部署服务

```bash
bash scripts/deploy.sh
```

### 3. 登录微信公众号平台

```bash
# 运行登录脚本
python3 scripts/login.py
```

脚本会：
1. 生成登录二维码
2. 提供多种访问方式（浏览器、文件路径）
3. 等待扫码登录
4. 自动检测登录状态

**⚠️ 重要**：必须使用**公众号**登录方式（不是小程序）

### 4. 添加公众号

```bash
python3 scripts/add_mp.py "新智元"
python3 scripts/add_mp.py "量子位"
```

### 5. 抓取文章

```bash
# 抓取所有公众号
python3 scripts/fetch_articles.py --all

# 抓取指定公众号
python3 scripts/fetch_articles.py --mp "新智元"
```

### 6. 查看统计

```bash
python3 scripts/show_stats.py
```

## 系统要求

- Docker 20.10+
- Python 3.8+
- 开放端口 4000

## 安装依赖

```bash
pip install requests
```

## 详细文档

请参阅 [SKILL.md](SKILL.md) 获取完整的使用指南。

## 工作流程

```
部署服务 → 扫码登录 → 添加公众号 → 抓取文章 → 查看统计
```

## 常见问题

**Q: 二维码扫描后显示登录成功，但搜索失败？**  
A: 请确保使用**公众号**登录方式，而不是小程序或其他方式。运行 `python3 scripts/fix_issues.py` 检查问题。

**Q: Docker 镜像拉取失败怎么办？**  
A: 部署脚本会提示使用国内镜像源或代理。也可以手动配置 Docker 镜像源。

**Q: 如何获取公众号的 fake_id？**  
A: 使用搜索功能，从搜索结果中提取 `fakeid` 字段。

**Q: 文章保存在哪里？**  
A: 文章保存在 `data/db.db` SQLite 数据库中。

## 故障排除

详细故障排除指南请参阅 [SKILL.md](SKILL.md)，包含以下问题的解决方案：

- 🔴 登录后无法搜索/抓取文章（200002 错误）
- 🔴 Docker 镜像拉取失败（国内网络）
- 🔴 Token 类型错误
- 🔴 PyYAML 模块缺失
- 🔴 登录状态无法持久化

## 项目结构

```
wechat-mp-fetcher/
├── SKILL.md              # 详细使用指南（含故障排除）
├── README.md             # 本文件
├── scripts/              # 脚本目录
│   ├── deploy.sh         # 部署脚本（含国内镜像提示）
│   ├── login.py          # 🔥 登录脚本（生成二维码并等待登录）
│   ├── get_token.py      # 获取 Token
│   ├── add_mp.py         # 添加公众号
│   ├── fetch_articles.py # 抓取文章
│   ├── show_stats.py     # 显示统计
│   └── fix_issues.py     # 问题修复工具
├── data/                 # 数据目录
│   └── db.db             # SQLite 数据库
└── assets/               # 资源文件
```

## 技术栈

- [we-mp-rss](https://github.com/rachelos/we-mp-rss) - 微信公众号 RSS 服务
- Docker - 容器化部署
- SQLite - 数据存储
- Python - 脚本工具

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 致谢

- [we-mp-rss](https://github.com/rachelos/we-mp-rss) 项目提供核心功能
