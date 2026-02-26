#!/bin/bash
# 部署 we-mp-rss Docker 服务

set -e

echo "=== 微信公众号文章抓取工具部署脚本 ==="
echo ""

# 检查 Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装，请先安装 Docker"
    exit 1
fi

# 检查 Docker 是否运行
if ! docker info &> /dev/null; then
    echo "❌ Docker 未运行，请启动 Docker 服务"
    exit 1
fi

echo "✅ Docker 环境正常"

# 检查端口
if lsof -Pi :4000 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "⚠️ 端口 4000 已被占用，尝试停止现有容器..."
    docker stop we-mp-rss 2>/dev/null || true
    docker rm we-mp-rss 2>/dev/null || true
fi

# 创建数据目录
mkdir -p data

# 拉取镜像
echo ""
echo "📥 拉取 we-mp-rss 镜像..."
echo ""

# 尝试拉取镜像，如果失败则提示使用国内镜像
if ! docker pull rachelos/we-mp-rss:latest 2>&1; then
    echo ""
    echo "❌ 镜像拉取失败，可能是网络问题"
    echo ""
    echo "解决方案（任选一种）："
    echo ""
    echo "方案1：配置 Docker 国内镜像源"
    echo "  sudo mkdir -p /etc/docker"
    echo "  sudo tee /etc/docker/daemon.json <<-'EOF'"
    echo '  {'
    echo '    "registry-mirrors": ['
    echo '      "https://docker.mirrors.ustc.edu.cn",'
    echo '      "https://hub-mirror.c.163.com"'
    echo '    ]'
    echo '  }'
    echo "  EOF"
    echo "  sudo systemctl restart docker"
    echo ""
    echo "方案2：使用代理"
    echo "  export HTTP_PROXY=http://your-proxy:port"
    echo "  export HTTPS_PROXY=http://your-proxy:port"
    echo "  bash scripts/deploy.sh"
    echo ""
    echo "方案3：手动下载镜像"
    echo "  从其他渠道获取 we-mp-rss.tar 镜像文件"
    echo "  docker load -i we-mp-rss.tar"
    echo ""
    exit 1
fi

# 启动容器
echo ""
echo "🚀 启动 we-mp-rss 容器..."
docker run -d --name we-mp-rss \
  -p 4000:4000 \
  -e DATABASE_TYPE=sqlite \
  -e AUTH_CODE=wemp2024 \
  -v "$(pwd)/data:/app/data" \
  --restart unless-stopped \
  rachelos/we-mp-rss:latest

# 等待服务启动
echo ""
echo "⏳ 等待服务启动..."
sleep 10

# 检查服务状态
if curl -s http://localhost:4000/ > /dev/null; then
    echo ""
    echo "✅ 服务部署成功！"
    echo ""
    echo "访问地址: http://localhost:4000"
    echo ""
    echo "下一步:"
    echo "1. 访问 http://localhost:4000"
    echo "2. 使用微信扫描二维码登录"
    echo "3. 使用公众号方式登录微信公众号平台"
    echo ""
    echo "⚠️ 重要提示："
    echo "   必须使用'公众号'登录方式，不是小程序！"
    echo "   否则会出现 200002 错误无法搜索"
else
    echo ""
    echo "❌ 服务启动失败，请检查日志:"
    echo "docker logs we-mp-rss"
    exit 1
fi
