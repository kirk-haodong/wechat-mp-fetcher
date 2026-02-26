#!/usr/bin/env python3
"""
显示文章统计信息
"""

import sqlite3
from datetime import datetime

DB_PATH = "data/db.db"

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 统计文章数量
    cursor.execute("SELECT COUNT(*) FROM articles")
    total = cursor.fetchone()[0]
    print(f"📊 文章总数: {total}")
    
    if total == 0:
        print("\n暂无文章，请先运行 fetch_articles.py 抓取文章")
        conn.close()
        return
    
    # 按公众号统计
    cursor.execute('''
        SELECT mp_id, COUNT(*) as count 
        FROM articles 
        GROUP BY mp_id 
        ORDER BY count DESC
    ''')
    
    print("\n📰 各公众号文章数:")
    print("-" * 40)
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]} 篇")
    
    # 显示最新文章
    print("\n📝 最新10篇文章:")
    print("-" * 40)
    cursor.execute('''
        SELECT title, mp_id, publish_time 
        FROM articles 
        ORDER BY publish_time DESC 
        LIMIT 10
    ''')
    
    for i, row in enumerate(cursor.fetchall(), 1):
        ts = datetime.fromtimestamp(row[2]).strftime('%m-%d %H:%M')
        print(f"{i}. [{ts}] {row[1]}")
        print(f"   {row[0][:50]}...")
    
    conn.close()

if __name__ == "__main__":
    main()
