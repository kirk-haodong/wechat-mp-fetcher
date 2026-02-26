#!/usr/bin/env python3
"""
基于全文内容生成每日热点总结
"""

import sqlite3
import argparse
import re
from datetime import datetime, timedelta
from collections import Counter

# 公众号名称映射
MP_NAMES = {
    'MP_WXS_3271041950': '新智元',
    'MP_WXS_3236757533': '量子位',
    'MP_WXS_3073282833': '机器之心',
    'MP_WXS_3223096120': '数字生命卡兹克',
    'MP_WXS_3010319264': '十字路口Crossing',
    'MP_WXS_1304308441': '极客公园',
    'MP_WXS_3874762412': '深思圈',
    'MP_WXS_3081486433': '智东西',
    'MP_WXS_3075228534': 'DeepTech深科技',
}


def clean_html(content):
    """清理HTML标签"""
    if not content:
        return ""
    text = re.sub(r'<[^>]+?>', '', content)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_summary(content, length=200):
    """提取文章摘要"""
    text = clean_html(content)
    if len(text) <= length:
        return text
    return text[:length] + "..."


def extract_keywords(title, content):
    """提取关键词"""
    text = title + " " + clean_html(content)
    keywords = []
    
    keyword_mapping = {
        'OpenAI': ['OpenAI', 'ChatGPT', 'GPT', 'Claude'],
        '谷歌/Google': ['谷歌', 'Google', 'DeepMind', 'Gemini'],
        '英伟达': ['英伟达', 'NVIDIA'],
        '大模型': ['模型', '大模型', 'LLM', 'Foundation Model'],
        '融资': ['融资', '估值', '上市', 'IPO'],
        '人才': ['招聘', '跳槽', '加盟', '离职', '年薪'],
        '学术': ['论文', '研究', 'ICLR', 'NeurIPS', 'CVPR', 'ICML'],
        'AI技术': ['AI', '人工智能', '智能体', 'Agent'],
    }
    
    for category, words in keyword_mapping.items():
        if any(word in text for word in words):
            keywords.append(category)
    
    return keywords


def classify_article(title, content, keywords):
    """对文章进行分类"""
    text = title + " " + clean_html(content)
    
    if any(kw in text for kw in ['论文', '研究', 'ICLR', 'NeurIPS', 'CVPR', '学术']):
        return '学术研究'
    elif any(kw in text for kw in ['融资', '估值', '上市', '招聘', '跳槽', '加盟']):
        return '公司/人才动态'
    elif any(kw in text for kw in ['产品', '应用', '工具', '平台', '发布']):
        return '产品/应用'
    elif any(kw in text for kw in ['模型', '算法', 'AI', '智能体', 'Agent', 'GPT']):
        return '大模型/AI技术'
    else:
        return '其他'


def generate_summary(hours=24, days=None, db_path='./data/db.db'):
    """生成总结报告"""
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 计算时间范围
    now = datetime.now()
    if days:
        start_time = now - timedelta(days=days)
    else:
        start_time = now - timedelta(hours=hours)
    
    start_timestamp = int(start_time.timestamp())
    
    # 查询有内容的文章
    cursor.execute('''
        SELECT title, mp_id, content, publish_time, url
        FROM articles 
        WHERE publish_time > ? AND LENGTH(content) > 0
        ORDER BY publish_time DESC
    ''', (start_timestamp,))
    
    articles = cursor.fetchall()
    
    if not articles:
        print(f"过去{hours if hours else days}小时内没有抓取到文章")
        conn.close()
        return
    
    # 分类
    categories = {
        '大模型/AI技术': [],
        '公司/人才动态': [],
        '产品/应用': [],
        '学术研究': [],
        '其他': []
    }
    
    all_keywords = []
    
    for title, mp_id, content, pub_time, url in articles:
        ts = datetime.fromtimestamp(pub_time).strftime('%m-%d %H:%M')
        source = MP_NAMES.get(mp_id, mp_id)
        summary = extract_summary(content)
        keywords = extract_keywords(title, content)
        category = classify_article(title, content, keywords)
        
        categories[category].append({
            'title': title,
            'source': source,
            'time': ts,
            'summary': summary,
            'keywords': keywords,
            'url': url
        })
        
        all_keywords.extend(keywords)
    
    # 生成报告
    time_range = f"{hours}小时" if hours else f"{days}天"
    report = f"""### 📱 AI 每日热点 | {now.strftime('%Y年%m月%d日')}

**过去{time_range}共抓取 {len(articles)} 篇文章（有全文内容）**

"""
    
    for category, items in categories.items():
        if items:
            report += f"\n## {category}\n\n"
            for i, item in enumerate(items[:5], 1):
                report += f"{i}. **{item['title']}**\n"
                report += f"   📰 {item['source']} | 🕐 {item['time']}\n"
                if item['keywords']:
                    report += f"   🏷️ {' | '.join(item['keywords'])}\n"
                report += f"   📝 {item['summary']}\n"
                report += f"   🔗 {item['url']}\n\n"
    
    # 关键词统计
    keyword_counts = Counter(all_keywords)
    report += "\n### 🔥 热点关键词\n\n"
    for keyword, count in keyword_counts.most_common(10):
        report += f"- {keyword}: {count} 次\n"
    
    # 保存报告
    import os
    os.makedirs('./daily-news', exist_ok=True)
    report_path = f"./daily-news/daily-summary-{now.strftime('%Y-%m-%d')}.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    # 打印报告
    print(report)
    print(f"\n✅ 报告已保存: {report_path}")
    
    conn.close()


def main():
    parser = argparse.ArgumentParser(description='生成微信公众号文章每日热点总结')
    parser.add_argument('--hours', type=int, default=24, help='过去多少小时的文章（默认24）')
    parser.add_argument('--days', type=int, help='过去多少天的文章')
    parser.add_argument('--db', type=str, default='./data/db.db', help='数据库路径')
    
    args = parser.parse_args()
    
    generate_summary(
        hours=args.hours if not args.days else None,
        days=args.days,
        db_path=args.db
    )


if __name__ == '__main__':
    main()
