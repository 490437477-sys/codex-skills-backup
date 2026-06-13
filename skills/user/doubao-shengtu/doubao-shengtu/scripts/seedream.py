#!/usr/bin/env python3
"""火山方舟 Seedream 图片生成脚本"""

import requests
import base64
import os
import sys
from datetime import datetime

API_KEY = "ark-8ce58018-81da-4caa-ac27-bb344e084917-f25f8"
API_URL = "https://ark.cn-beijing.volces.com/api/plan/v3/images/generations"
MODEL = "doubao-seedream-5.0-lite"

def generate_image(prompt, output_path=None, size="1920x1920"):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "size": size,
        "response_format": "b64_json"
    }
    
    print(f"正在生成图片，提示词: {prompt}")
    resp = requests.post(API_URL, headers=headers, json=payload, timeout=120)
    
    if resp.status_code != 200:
        print(f"API 错误: {resp.status_code}")
        print(resp.text)
        return None
    
    data = resp.json()
    
    for i, img_data in enumerate(data.get("data", [])):
        b64 = img_data.get("b64_json", "")
        if not b64:
            continue
        
        img_bytes = base64.b64decode(b64)
        
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = f"seedream_{timestamp}.png"
        
        with open(output_path, "wb") as f:
            f.write(img_bytes)
        
        print(f"图片已保存: {output_path}")
        return output_path
    
    return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python seedream.py <提示词> [输出路径] [尺寸]")
        print("示例: python seedream.py '一位美丽的女孩，写实风格' output.png 1920x1920")
        sys.exit(1)
    
    prompt = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    size = sys.argv[3] if len(sys.argv) > 3 else "1920x1920"
    
    generate_image(prompt, out, size)
