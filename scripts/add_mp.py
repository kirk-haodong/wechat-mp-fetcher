#!/usr/bin/env python3
"""
添加公众号到数据库
"""

import sys
import requests
import json
import sqlite3
import base64
from datetime import datetime

API_BASE = "http://localhost:4000/api/v1/wx"
DB_PATH = "data/db.db"

def get_token():
    """获取访问 Token"""
    import subprocess
    result = subprocess.run(
        ["python3", "scripts/get_token.py"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def search_mp(name, token):
    """搜索公众号"""
    url = f"{API_BASE}/mps/search/{name}?limit=5"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        result = response.json()
        
        if "data" in result and "list" in result["data"]:
            return result["data"]["list"]
        else:
            print(f"搜索失败: {result}")
            return []
    except Exception as e:
        print(f"请求失败: {e}")
        return []

def add_to_db(fake_id, name, intro):
    """添加公众号到数据库"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 生成 ID
    try:
        fake_id_decoded = base64.b64decode(fake_id).decode('utf-8')
        mp_id = f"MP_WXS_{fake_id_decoded}"
    except:
        mp_id = f"MP_WXS_{fake_id.replace('=', '_')}"
    
    now = datetime.now().isoformat()
    
    # 检查是否已存在
    cursor.execute('SELECT id FROM feeds WHERE faker_id = ?', (fake_id,))
    if cursor.fetchone():
        print(f"⚠️ 公众号 '{name}' 已存在")
        conn.close()
        return False
    
    # 插入新记录
    cursor.execute('''
        INSERT INTO feeds (id, mp_name, mp_cover, mp_intro, status, created_at, updated_at, faker_id, update_time, sync_time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        mp_id, name, '/static/default-avatar.png', intro, 1, now, now, fake_id, 0, 0
    ))
    
    conn.commit()
    conn.close()
    return True

def main():
    if len(sys.argv) < 2:
        print("用法: python3 add_mp.py \"公众号名称\"")
        sys.exit(1)
    
    name = sys.argv[1]
    print(f"🔍 搜索公众号: {name}")
    
    # 获取 Token
    token = get_token()
    if not token:
        print("❌ 获取 Token 失败")
        sys.exit(1)
    
    # 搜索公众号
    results = search_mp(name, token)
    if not results:
        print(f"❌ 未找到公众号: {name}")
        sys.exit(1)
    
    # 显示搜索结果
    print(f"\n找到 {len(results)} 个结果:")
    for i, item in enumerate(results, 1):
        print(f"{i}. {item.get('nickname')} ({item.get('alias', '无别名')})")
        print(f"   fakeid: {item.get('fakeid')}")
        print(f"   简介: {item.get('signature', '无')[:50]}...")
        print()
    
    # 添加第一个结果
    item = results[0]
    fake_id = item.get('fakeid')
    nickname = item.get('nickname')
    signature = item.get('signature', '')
    
    print(f"✅ 添加公众号: {nickname}")
    if add_to_db(fake_id, nickname, signature):
        print(f"✅ 添加成功!")
        print(f"   fake_id: {fake_id}")
    else:
        print(f"⚠️ 添加失败或已存在")

if __name__ == "__main__":
    main()
