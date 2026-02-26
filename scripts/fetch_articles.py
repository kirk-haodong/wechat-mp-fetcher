#!/usr/bin/env python3
"""
抓取公众号文章
"""

import sys
import argparse
import requests
import json
import sqlite3
import subprocess
import time

API_BASE = "http://localhost:4000/api/v1/wx"
DB_PATH = "data/db.db"

def get_token():
    """获取访问 Token"""
    result = subprocess.run(
        ["python3", "scripts/get_token.py"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def get_all_mps():
    """获取所有公众号"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, mp_name FROM feeds WHERE status = 1")
    results = cursor.fetchall()
    conn.close()
    return results

def fetch_articles(mp_id, token, pages=1):
    """抓取文章"""
    url = f"{API_BASE}/mps/update/{mp_id}?start_page=0&end_page={pages}"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(url, headers=headers, timeout=60)
        result = response.json()
        return result
    except Exception as e:
        print(f"请求失败: {e}")
        return None

def get_article_count():
    """获取文章总数"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM articles")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def main():
    parser = argparse.ArgumentParser(description="抓取公众号文章")
    parser.add_argument("--all", action="store_true", help="抓取所有公众号")
    parser.add_argument("--mp", type=str, help="指定公众号名称")
    parser.add_argument("--pages", type=int, default=1, help="抓取页数 (默认: 1)")
    args = parser.parse_args()
    
    # 获取 Token
    token = get_token()
    if not token:
        print("❌ 获取 Token 失败")
        sys.exit(1)
    
    # 获取要抓取的公众号列表
    if args.all:
        mps = get_all_mps()
        print(f"📋 共 {len(mps)} 个公众号需要抓取")
    elif args.mp:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, mp_name FROM feeds WHERE mp_name = ? AND status = 1", (args.mp,))
        mps = cursor.fetchall()
        conn.close()
        if not mps:
            print(f"❌ 未找到公众号: {args.mp}")
            sys.exit(1)
    else:
        print("❌ 请指定 --all 或 --mp \"公众号名称\"")
        sys.exit(1)
    
    # 抓取文章
    total_added = 0
    initial_count = get_article_count()
    
    for mp_id, mp_name in mps:
        print(f"\n📰 抓取: {mp_name}")
        result = fetch_articles(mp_id, token, args.pages)
        
        if result and "data" in result:
            print(f"   ✅ 抓取任务已触发")
        else:
            print(f"   ❌ 抓取失败")
        
        # 等待一下，避免请求过快
        time.sleep(2)
    
    # 等待抓取完成
    print("\n⏳ 等待抓取完成...")
    time.sleep(15)
    
    # 显示结果
    final_count = get_article_count()
    added = final_count - initial_count
    
    print(f"\n✅ 抓取完成!")
    print(f"   新增文章: {added} 篇")
    print(f"   文章总数: {final_count} 篇")

if __name__ == "__main__":
    main()
