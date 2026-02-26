#!/usr/bin/env python3
"""
生成并显示登录二维码
支持多种方式：终端显示、保存图片、Base64编码
"""

import requests
import subprocess
import sys
import os
import time

API_BASE = "http://localhost:4000/api/v1/wx"

def get_token():
    """获取访问 Token"""
    result = subprocess.run(
        ["python3", "scripts/get_token.py"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def generate_qr(token):
    """生成二维码"""
    url = f"{API_BASE}/auth/qr/code"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        result = response.json()
        
        if result.get("code") == 0:
            return True
        else:
            print(f"生成二维码失败: {result}")
            return False
    except Exception as e:
        print(f"请求失败: {e}")
        return False

def show_qr_options():
    """显示二维码访问方式"""
    print("\n" + "="*60)
    print("📱 微信登录二维码")
    print("="*60)
    print()
    print("方式1：浏览器访问")
    print("  http://localhost:4000/static/wx_qrcode.png")
    print()
    print("方式2：本地文件路径")
    print("  ./data/wx_qrcode.png")
    print()
    print("方式3：使用 Python 显示在终端")
    print("  python3 -c \"from PIL import Image; Image.open('data/wx_qrcode.png').show()\"")
    print()
    print("="*60)
    print("⚠️  重要提示：")
    print("   1. 使用微信扫描二维码")
    print("   2. 选择'公众号'登录方式（不是小程序！）")
    print("   3. 点击确认登录")
    print("="*60)

def check_login_status(token):
    """检查登录状态"""
    url = f"{API_BASE}/auth/qr/status"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        result = response.json()
        
        if result.get("data", {}).get("login_status"):
            return True
        return False
    except:
        return False

def wait_for_login(token, timeout=300):
    """等待用户登录"""
    print("\n⏳ 等待扫码登录...")
    print(f"   超时时间: {timeout} 秒")
    print()
    
    for i in range(timeout):
        if check_login_status(token):
            print("\n✅ 登录成功！")
            return True
        
        if i % 10 == 0:
            print(f"   已等待 {i} 秒...", end="\r")
        
        time.sleep(1)
    
    print("\n❌ 登录超时")
    return False

def main():
    print("=== 微信登录二维码生成 ===")
    print()
    
    # 检查服务是否运行
    try:
        response = requests.get("http://localhost:4000/", timeout=5)
    except:
        print("❌ 服务未运行，请先部署:")
        print("   bash scripts/deploy.sh")
        sys.exit(1)
    
    # 获取 Token
    token = get_token()
    if not token:
        print("❌ 获取 Token 失败")
        sys.exit(1)
    
    # 生成二维码
    if not generate_qr(token):
        print("❌ 生成二维码失败")
        sys.exit(1)
    
    # 等待二维码文件生成
    time.sleep(3)
    
    # 显示二维码访问方式
    show_qr_options()
    
    # 等待登录
    if wait_for_login(token):
        print("\n🎉 可以开始添加公众号并抓取文章了！")
        print()
        print("示例命令:")
        print("  python3 scripts/add_mp.py \"新智元\"")
        print("  python3 scripts/fetch_articles.py --all")
    else:
        print("\n⚠️ 登录未完成，请重新运行本脚本")
        sys.exit(1)

if __name__ == "__main__":
    main()
