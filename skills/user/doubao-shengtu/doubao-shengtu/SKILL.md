---
name: doubao-shengtu
description: 使用字节跳动火山方舟 Seedream API 生成高质量图片。当用户需要生成图片、创作图像、文生图、豆包生图、或使用 Seedream/火山方舟/豆包生成图片时使用。支持 doubao-seedream-5.0-lite 模型。
---

# 火山方舟 Seedream 图片生成

使用字节跳动火山方舟 (Ark) 的 Seedream 模型生成图片。

## API 配置

- 端点: `https://ark.cn-beijing.volces.com/api/plan/v3/images/generations`
- 模型: `doubao-seedream-5.0-lite`
- API Key: `ark-8ce58018-81da-4caa-ac27-bb344e084917-f25f8`
- 最小尺寸: 3686400 像素 (如 1920x1920)

## 使用方法

调用 `scripts/seedream.py` 脚本生成图片:

```bash
python scripts/seedream.py "<提示词>" "<输出路径>" "<尺寸>"
```

### 参数说明
- 提示词: 图片描述，支持中文和英文
- 输出路径: 保存图片的路径，默认为 `seedream_时间戳.png`
- 尺寸: 图片尺寸，默认 `1920x1920`，最小 3686400 像素

### 示例
```bash
python scripts/seedream.py "一位美丽的亚洲女孩，写实摄影风格" "beauty.png" "1920x1920"
```

## 注意事项
- 需要网络访问 `ark.cn-beijing.volces.com`
- 生成时间约 10-30 秒
- 支持格式: PNG
