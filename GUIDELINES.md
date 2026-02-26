# GitHub 提交风格指南

本文档定义了 kirk-haodong 的 GitHub 项目提交风格规范，确保所有项目保持一致的专业外观。

---

## 📐 README 排版规范

### 1. 顶部布局（从上到下）

```markdown
<p align="center">
  <img src="[Logo URL]" alt="[Project Name]" width="180">
</p>

<h1 align="center">[Project Name]</h1>

<p align="center">
  [Badges]
</p>

<p align="center">
  [Language Switch Links]
</p>

<p align="center">
  [One-line description]
</p>

---
```

### 2. Badges 规范

必须包含的 badges（按顺序）：

```markdown
<a href="https://www.python.org/downloads/">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
</a>
<a href="https://github.com/kirk-haodong/[repo]/blob/master/LICENSE">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
</a>
<a href="https://github.com/kirk-haodong/[repo]/stargazers">
  <img src="https://img.shields.io/github/stars/kirk-haodong/[repo].svg?style=social" alt="GitHub stars">
</a>
```

可选 badges：
- Docker version: `https://img.shields.io/badge/docker-20.10+-blue.svg`
- Build status: `https://img.shields.io/badge/build-passing-brightgreen.svg`
- Version: `https://img.shields.io/badge/version-1.0.0-blue.svg`

### 3. 语言切换规范

```markdown
<p align="center">
  <a href="README.md">English</a> •
  <a href="README.zh.md">中文</a> •
  <a href="README.ja.md">日本語</a>
</p>
```

**文件命名规范：**
- 英文（默认）: `README.md`
- 中文: `README.zh.md`
- 日文: `README.ja.md`
- 其他语言: `README.[语言代码].md`

### 4. 章节结构

```markdown
## ✨ Features / 功能特性 / 機能

## 🚀 Quick Start / 快速开始 / クイックスタート

## 📁 Project Structure / 项目结构 / プロジェクト構造

## 🛠️ Troubleshooting / 故障排除 / トラブルシューティング

## 📄 License / 许可证 / ライセンス

## 🙏 Acknowledgments / 致谢 / 謝辞
```

### 5. 图标使用规范

常用图标及含义：

| 图标 | 用途 |
|------|------|
| 🐳 | Docker 相关 |
| 📱 | 移动端/扫码 |
| 🔍 | 搜索功能 |
| 📄 | 文档/文章 |
| 📊 | 统计/数据 |
| 🔧 | 工具/设置 |
| ⚠️ | 警告/重要提示 |
| ✅ | 完成/成功 |
| ❌ | 错误/失败 |
| 🎉 | 庆祝/完成 |
| ✨ | 功能特性 |
| 🚀 | 快速开始 |
| 📁 | 项目结构 |
| 🛠️ | 故障排除 |
| 📄 | 许可证 |
| 🙏 | 致谢 |

---

## 📝 Git 提交规范

### 提交信息格式

```
[type]: [subject]

[body]
```

### Type 规范

| Type | 用途 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat: Add login script` |
| `fix` | 修复 bug | `fix: Resolve 200002 error` |
| `docs` | 文档更新 | `docs: Update README` |
| `style` | 格式调整 | `style: Format code` |
| `refactor` | 重构 | `refactor: Optimize fetch logic` |
| `test` | 测试 | `test: Add unit tests` |
| `chore` | 构建/工具 | `chore: Update dependencies` |
| `design` | UI/设计 | `design: Redesign README layout` |

### Subject 规范

- 使用现在时态（Add, not Added）
- 首字母大写
- 不超过 50 个字符
- 不加句号

### Body 规范（可选）

- 详细描述变更内容
- 每行不超过 72 个字符
- 说明变更原因和方式

### 示例

```bash
# 好的提交信息
git commit -m "feat: Add multi-language support for README"

git commit -m "fix: Resolve Docker image pull timeout issue

- Add domestic mirror configuration
- Add proxy support
- Update deploy script with better error handling"

git commit -m "design: Redesign README with badges and centered layout

- Move logo to top center
- Add Python version and license badges
- Split into EN/ZH/JP files"
```

---

## 🎨 视觉规范

### Logo 规范

- 尺寸：180px 宽度（显示尺寸）
- 格式：同时提供 PNG 和 SVG
- 位置：`assets/logo.png` 和 `assets/logo.svg`
- 背景：圆角矩形，主色调

### 颜色规范

- 成功/通过：绿色 (#28a745)
- 信息/提示：蓝色 (#007bff)
- 警告：黄色 (#ffc107)
- 错误：红色 (#dc3545)

### 排版规范

- 标题层级：h1 (居中) → h2 → h3
- 代码块：指定语言类型
- 列表：使用 `-` 或 `1.`
- 强调：使用 `**粗体**` 或 `_斜体_`

---

## 📂 文件结构规范

```
project-name/
├── README.md              # 英文文档（默认）
├── README.zh.md           # 中文文档
├── README.ja.md           # 日文文档
├── LICENSE                # MIT 许可证
├── SKILL.md               # OpenClaw Skill 文档（如适用）
├── scripts/               # 脚本目录
│   └── *.py / *.sh
├── assets/                # 资源文件
│   ├── logo.png
│   └── logo.svg
└── data/                  # 数据目录（如适用）
```

---

## 🔗 链接规范

### 内部链接

```markdown
# 相对路径
[SKILL.md](SKILL.md)
[Logo](assets/logo.png)

# 绝对路径（用于显示图片）
<img src="https://github.com/kirk-haodong/[repo]/blob/master/assets/logo.png?raw=true">
```

### 外部链接

```markdown
# 项目引用
[we-mp-rss](https://github.com/rachelos/we-mp-rss)

# 徽章链接
<a href="https://www.python.org/downloads/">
  <img src="...">
</a>
```

---

## ✅ 发布前检查清单

- [ ] Logo 已添加到 `assets/` 目录（PNG + SVG）
- [ ] README 包含 badges（Python、License、Stars）
- [ ] 语言切换链接正常工作
- [ ] 所有章节图标统一
- [ ] 代码块指定了语言类型
- [ ] 提交信息符合规范
- [ ] 已推送到 GitHub
- [ ] GitHub 页面显示正常

---

## 📝 示例模板

见 `templates/README.template.md`

---

**最后更新：** 2026-02-26
**版本：** 1.0.0
**作者：** kirk-haodong
