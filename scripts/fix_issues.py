#!/usr/bin/env python3
"""
修复 we-mp-rss 常见问题
"""

import subprocess
import sys

def fix_pyyaml():
    """修复 PyYAML 模块缺失问题"""
    print("🔧 检查 PyYAML 模块...")
    
    # 检查容器内是否已安装 PyYAML
    result = subprocess.run(
        ["docker", "exec", "we-mp-rss", "python3", "-c", "import yaml; print('ok')"],
        capture_output=True,
        text=True
    )
    
    if "ok" in result.stdout:
        print("✅ PyYAML 已安装")
        return True
    
    print("⚠️ PyYAML 未安装，正在安装...")
    
    # 安装 PyYAML
    install_result = subprocess.run(
        ["docker", "exec", "we-mp-rss", "pip", "install", "pyyaml", "-q"],
        capture_output=True,
        text=True
    )
    
    if install_result.returncode == 0:
        print("✅ PyYAML 安装成功")
        
        # 重启容器
        print("🔄 重启容器...")
        subprocess.run(["docker", "restart", "we-mp-rss"], capture_output=True)
        print("✅ 容器已重启")
        return True
    else:
        print(f"❌ PyYAML 安装失败: {install_result.stderr}")
        return False

def fix_login_status():
    """修复登录状态持久化"""
    print("🔧 检查登录状态持久化...")
    
    import sqlite3
    import os
    
    db_path = "data/db.db"
    if not os.path.exists(db_path):
        print(f"⚠️ 数据库不存在: {db_path}")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 检查表是否存在
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='wx_login_status'")
    if cursor.fetchone():
        print("✅ 登录状态表已存在")
        conn.close()
        return True
    
    # 创建表
    print("📝 创建登录状态表...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wx_login_status (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            is_logged_in BOOLEAN DEFAULT 0,
            login_time INTEGER,
            expiry_time INTEGER,
            token TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute("INSERT OR IGNORE INTO wx_login_status (id, is_logged_in) VALUES (1, 0)")
    conn.commit()
    conn.close()
    
    print("✅ 登录状态表创建成功")
    return True

def main():
    print("=== we-mp-rss 问题修复工具 ===")
    print("")
    
    # 检查容器是否运行
    result = subprocess.run(
        ["docker", "ps", "-q", "-f", "name=we-mp-rss"],
        capture_output=True,
        text=True
    )
    
    if not result.stdout.strip():
        print("❌ we-mp-rss 容器未运行，请先部署服务")
        print("   bash scripts/deploy.sh")
        sys.exit(1)
    
    print("✅ 容器运行正常")
    print("")
    
    # 执行修复
    fixes = [
        ("PyYAML 模块", fix_pyyaml),
        ("登录状态持久化", fix_login_status),
    ]
    
    success_count = 0
    for name, fix_func in fixes:
        print(f"\n[{name}]")
        if fix_func():
            success_count += 1
    
    print(f"\n✅ 修复完成: {success_count}/{len(fixes)} 项成功")
    
    if success_count < len(fixes):
        print("⚠️ 部分修复失败，请查看上方日志")
        sys.exit(1)

if __name__ == "__main__":
    main()
