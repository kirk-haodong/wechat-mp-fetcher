#!/usr/bin/env python3
"""
获取 API 访问 Token
"""

import requests
import json

API_BASE = "http://localhost:4000/api/v1/wx"
USERNAME = "admin"
PASSWORD = "wemp2024"

def get_token():
    """获取访问 Token"""
    url = f"{API_BASE}/auth/token"
    data = {
        "username": USERNAME,
        "password": PASSWORD
    }
    
    try:
        response = requests.post(url, data=data, timeout=10)
        result = response.json()
        
        if "access_token" in result:
            return result["access_token"]
        else:
            print(f"获取 Token 失败: {result}")
            return None
    except Exception as e:
        print(f"请求失败: {e}")
        return None

if __name__ == "__main__":
    token = get_token()
    if token:
        print(token)
    else:
        exit(1)
