---
name: baiditu
description: 调用阿里云视觉智能平台（imageseg.cn-shanghai）对图片进行主体分割，输出白底图、透明 PNG 或裁剪图。默认在源目录创建「白底图」子目录保存结果。支持商品分割、人体分割、通用分割、食品分割、服饰分割、Logo 分割、车辆分割、动物分割、天空分割、高清通用分割共 10 种模型。当用户需要对图片进行抠图、去背景、制作商品白底图、人像分割、Logo 提取等任务时使用此技能。
---

# 白底图

通过阿里云视觉智能开放平台对图片进行主体分割，输出白底图、透明 PNG 或裁剪图。  
**默认行为：在源目录（或源文件同目录）下创建 `白底图` 子目录存放结果**，可用 `-o` 覆盖。

## 默认输出位置

| 输入 | 默认输出目录 |
|------|-------------|
| 目录 `./photos/` | `./photos/白底图/` |
| 文件 `./photos/a.jpg` | `./photos/白底图/a.jpg` |

需要输出到其他位置时用 `-o /path/to/out` 显式指定。

## 前置条件

```bash
pip install alibabacloud_imageseg20191230 alibabacloud_tea_openapi alibabacloud_tea_util Pillow
```

## 配置凭证

优先用环境变量，未设置时使用脚本内置占位（生产环境务必改为环境变量）：

```bash
setx ALIBABA_CLOUD_ACCESS_KEY_ID "你的Key"
setx ALIBABA_CLOUD_ACCESS_KEY_SECRET "你的Secret"
```

## 使用方式

直接运行 `scripts/aliyun_seg.py`。

### 目录批量（默认输出到 `源目录/白底图`）

```bash
python scripts/aliyun_seg.py ./photos                      # 批量商品分割 + 白底图
python scripts/aliyun_seg.py ./photos -m body              # 人体分割
python scripts/aliyun_seg.py ./photos -f mask              # 透明背景 PNG
python scripts/aliyun_seg.py ./photos -o ./out -f crop     # 裁剪到主体区域，输出到 ./out
```

### 单张图片（默认输出到 `源文件同目录/白底图`）

```bash
python scripts/aliyun_seg.py ./photos/a.jpg                # → ./photos/白底图/a.jpg
python scripts/aliyun_seg.py ./photos/a.jpg -o result.png  # → ./result.png
```

### 工具

```bash
python scripts/aliyun_seg.py --list-models                 # 列出所有支持的模型
```

## 支持的模型

| 模型 | 说明 | 返回格式 |
|------|------|---------|
| `commodity` | 商品分割（白底图首选） | whiteBK / mask / crop |
| `common` | 通用分割 | whiteBK / mask / crop |
| `body` | 人体分割 | whiteBK / mask / crop |
| `food` | 食品分割 | whiteBK / mask / crop |
| `animal` | 动物分割 | whiteBK / mask / crop |
| `hd_common` | 高清通用分割 | 仅分割结果图 |
| `cloth` | 服饰分割 | 仅分割结果图 |
| `logo` | Logo 分割 | 仅分割结果图 |
| `vehicle` | 车辆分割 | 仅分割结果图 |
| `sky` | 天空分割 | 仅分割结果图 |

## 返回格式

- `whiteBK` — 白色背景（默认，最常用）
- `mask` — 透明背景 PNG
- `crop` — 裁剪到主体边界框

## 内部流程（出错时可参考）

1. Pillow 检查图片最长边，超过 2000px 等比缩放（阿里云硬性限制 ≤ 2000×2000）
2. 用 `*AdvanceRequest.image_urlobject = open(...)` 上传二进制
3. 调用 `client.segment_xxx_advance(req, runtime)`
4. `resp.body.data.image_url` 是带签名的 OSS CDN URL，用 `urllib.request.urlretrieve` 下载到本地
5. 输出文件名沿用源文件 stem，扩展名随返回格式（mask→png，否则同源）

## 注意事项

- 图片超过 2000×2000 时脚本会自动缩放，原始分辨率不被保留
- 透明背景（mask）输出扩展名为 .png，其他沿用输入扩展名
- 凭证硬编码在脚本中仅作占位，生产环境建议改用环境变量
- 支持 PNG / JPG / JPEG / WebP / BMP 输入
- 网络：脚本会下载阿里云返回的签名 URL，机器需能访问公网