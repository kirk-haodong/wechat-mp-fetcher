---
name: wechat-mp-fetcher
description: 微信公众号文章抓取工具 - 通过 Docker 部署 we-mp-rss 服务，用户扫码登录微信公众号平台后，可搜索并抓取指定公众号的文章。Use when user needs to fetch WeChat Official Account articles, configure WeChat MP RSS service, or manage WeChat public account content fetching.
metadata:
  openclaw:
    emoji: "📰"
    category: "content"
    tags: ["wechat", "mp", "rss", "article", "fetch", "docker"]
---

# 微信公众号文章抓取工具

自动部署 we-mp-rss 服务，通过微信公众号平台登录，抓取指定公众号的文章内容。

## 功能

- 🐳 Docker 自动部署 we-mp-rss 服务
- 📱 微信公众号平台扫码登录
- 🔍 搜索并添加公众号
- 📄 自动抓取文章内容
- 📊 文章统计与管理

## 前置要求

- Docker 已安装并运行
- 用户拥有微信公众号平台账号（需登录 mp.weixin.qq.com）
- 开放 4000 端口

## 快速开始

### 1. 部署服务

```bash
# 运行部署脚本
bash scripts/deploy.sh
```

脚本会自动：
- 拉取 we-mp-rss Docker 镜像
- 启动容器并配置环境
- 等待服务就绪

### 2. 用户登录

1. 访问 `http://localhost:4000`
2. 使用微信扫描二维码
3. **重要**：必须使用公众号登录微信公众号平台（mp.weixin.qq.com）
4. 点击确认登录

### 3. 添加公众号

```bash
# 使用脚本添加公众号
python3 scripts/add_mp.py "公众号名称"

# 示例
python3 scripts/add_mp.py "新智元"
python3 scripts/add_mp.py "量子位"
```

### 4. 抓取文章

```bash
# 抓取所有公众号文章
python3 scripts/fetch_articles.py --all

# 抓取指定公众号
python3 scripts/fetch_articles.py --mp "新智元"

# 指定抓取页数
python3 scripts/fetch_articles.py --mp "新智元" --pages 2
```

## 详细工作流程

### 部署流程

1. **检查 Docker 环境**
   - 验证 Docker 是否安装
   - 检查端口 4000 是否可用

2. **启动 we-mp-rss 容器**
   ```bash
   docker run -d --name we-mp-rss \
     -p 4000:4000 \
     -e DATABASE_TYPE=sqlite \
     -e AUTH_CODE=wemp2024 \
     -v ./data:/app/data \
     --restart unless-stopped \
     rachelos/we-mp-rss:latest
   ```

3. **验证服务状态**
   - 等待服务启动（约 10 秒）
   - 访问 `http://localhost:4000` 确认

### 登录流程

1. **获取登录二维码**
   ```bash
   curl -s "http://localhost:4000/api/v1/wx/auth/qr/code" \
     -H "Authorization: Bearer $(python3 scripts/get_token.py)"
   ```

2. **用户扫码**
   - 打开 `http://localhost:4000/static/wx_qrcode.png`
   - 使用微信扫描
   - **关键**：选择"公众号"登录方式
   - 确认登录

3. **验证登录状态**
   ```bash
   curl -s "http://localhost:4000/api/v1/wx/auth/qr/status" \
     -H "Authorization: Bearer $(python3 scripts/get_token.py)"
   ```

### 添加公众号流程

1. **搜索公众号**
   ```bash
   curl -s "http://localhost:4000/api/v1/wx/mps/search/公众号名称?limit=5" \
     -H "Authorization: Bearer $(python3 scripts/get_token.py)"
   ```

2. **提取 fake_id**
   - 从搜索结果中获取 `fakeid` 字段
   - 示例：`MzI3MTA0MTk1MA==`

3. **添加到数据库**
   - 使用 `scripts/add_mp.py` 自动完成

### 文章抓取流程

1. **触发抓取任务**
   ```bash
   curl -s "http://localhost:4000/api/v1/wx/mps/update/{mp_id}?start_page=0&end_page=2" \
     -H "Authorization: Bearer $(python3 scripts/get_token.py)"
   ```

2. **查看抓取进度**
   ```bash
   docker logs we-mp-rss --tail 20
   ```

3. **验证文章保存**
   - 文章保存到 SQLite 数据库
   - 查看 `data/db.db` 中的 `articles` 表

## 脚本说明

### deploy.sh
部署 we-mp-rss Docker 服务

```bash
bash scripts/deploy.sh
```

### get_token.py
获取 API 访问 Token

```python
python3 scripts/get_token.py
# 输出: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### add_mp.py
添加公众号到数据库

```bash
python3 scripts/add_mp.py "公众号名称"
```

### fetch_articles.py
抓取文章

```bash
# 抓取所有
python3 scripts/fetch_articles.py --all

# 抓取指定公众号
python3 scripts/fetch_articles.py --mp "新智元"

# 指定页数
python3 scripts/fetch_articles.py --mp "新智元" --pages 2
```

### show_stats.py
显示统计信息

```bash
python3 scripts/show_stats.py
```

## 故障排除与经验总结

### 🔴 问题1：登录后无法搜索/抓取文章（返回 200002 错误）

**现象**：
- 扫码显示"登录成功"
- 但搜索时返回 `{"base_resp":{"ret":200002,"err_msg":"invalid args"}}`

**原因**：
- 使用了错误的登录方式（如小程序后台）
- 必须使用**公众号**方式登录 mp.weixin.qq.com

**解决**：
1. 重新扫码登录
2. **关键**：在微信中选择"公众号"登录方式
3. 确认登录后等待 5 秒再测试

**验证方法**：
```bash
# 检查登录状态
curl -s "http://localhost:4000/api/v1/wx/auth/qr/status" \
  -H "Authorization: Bearer $(python3 scripts/get_token.py)"

# 预期输出：{"login_status": true}
```

---

### 🔴 问题2：Docker 镜像拉取失败（国内网络）

**现象**：
```
Error response from daemon: pull access denied for rachelos/we-mp-rss
```

**原因**：
- 国内网络访问 Docker Hub 受限

**解决**（任选一种）：

**方案 A：使用国内镜像源**
```bash
# 配置 Docker 国内镜像
cat > /etc/docker/daemon.json << 'EOF'
{
  "registry-mirrors": [
    "https://docker.mirrors.ustc.edu.cn",
    "https://hub-mirror.c.163.com"
  ]
}
EOF
systemctl restart docker
```

**方案 B：手动下载镜像**
```bash
# 从其他渠道下载镜像文件
docker load -i we-mp-rss.tar
```

**方案 C：使用代理**
```bash
# 配置 Docker 代理
export HTTP_PROXY=http://your-proxy:port
docker pull rachelos/we-mp-rss:latest
```

---

### 🔴 问题3：Token 类型错误导致搜索失败

**现象**：
- 搜索返回 200002 错误
- 日志显示 `token: 306867159`（整数而非字符串）

**原因**：
- we-mp-rss 早期版本将 token 作为整数传递
- 微信 API 要求 token 必须是字符串

**解决**：
已在本 Skill 的脚本中修复，确保 token 以字符串形式传递：
```python
params = {
    "token": str(token),  # 强制转换为字符串
    ...
}
```

---

### 🔴 问题4：PyYAML 模块缺失

**现象**：
```
ModuleNotFoundError: No module named 'yaml'
```

**原因**：
- we-mp-rss 容器内未安装 PyYAML
- 导致无法解析 `wx.lic` 配置文件

**解决**：
```bash
# 进入容器安装 PyYAML
docker exec we-mp-rss pip install pyyaml

# 重启容器
docker restart we-mp-rss
```

---

### 🔴 问题5：登录状态无法持久化

**现象**：
- 登录成功后一段时间（几分钟）后失效
- 需要频繁重新扫码

**原因**：
- we-mp-rss 默认将登录状态保存在内存中
- 服务重启或重新初始化后状态丢失

**解决**：
已在本 Skill 中修复，修改 `success.py` 将登录状态持久化到数据库：
- 登录状态保存到 `wx_login_status` 表
- Token 和 Cookie 保存到 `wx.lic` 文件
- 重启服务后自动恢复登录状态

---

## 常见问题

### Q: 二维码扫描后显示登录成功，但搜索失败？
A: 请确保使用**公众号**登录方式，而不是小程序或其他方式。参考"问题1"。

### Q: Docker 镜像拉取失败怎么办？
A: 参考"问题2"，使用国内镜像源或代理。

### Q: 如何获取公众号的 fake_id？
A: 使用搜索功能，从搜索结果中提取 `fakeid` 字段。

### Q: 文章保存在哪里？
A: 文章保存在 `data/db.db` SQLite 数据库中，表名为 `articles`。

### Q: 如何查看抓取的文章？
A: 使用 `scripts/show_stats.py` 或直接在数据库中查询。

### Q: 登录状态会过期吗？
A: 会，通常几天后需要重新登录。重新运行登录流程即可。

## 数据结构

### 公众号表 (feeds)

| 字段 | 说明 |
|------|------|
| id | 公众号唯一ID |
| mp_name | 公众号名称 |
| faker_id | 微信 fake_id |
| mp_intro | 简介 |
| status | 状态 (1=启用) |

### 文章表 (articles)

| 字段 | 说明 |
|------|------|
| id | 文章唯一ID |
| mp_id | 所属公众号ID |
| title | 文章标题 |
| content | 文章内容 |
| publish_time | 发布时间 |
| url | 文章链接 |

## 参考

- we-mp-rss 项目: https://github.com/rachelos/we-mp-rss
- 微信公众号平台: https://mp.weixin.qq.com
