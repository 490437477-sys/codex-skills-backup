---
name: baiditu
description: 调用阿里云视觉智能平台进行图片主体分割，输出白底图、透明PNG或裁剪图。支持商品分割、人体分割、通用分割、食品分割、服饰分割、Logo分割、车辆分割、动物分割、天空分割、高清通用分割共10种模型。当用户需要对图片进行抠图、去背景、商品白底图制作、人像分割等任务时使用此技能。
---

# 白底图

通过阿里云视觉智能平台 API 对图片进行主体分割，支持 10 种分割模型，输出白底图、透明 PNG 或裁剪图。

## 前置条件

确保已安装依赖：

```bash
pip install alibabacloud_imageseg20191230 alibabacloud_tea_openapi alibabacloud_tea_util
```

## 使用方式

运行 `scripts/aliyun_seg.py`，首次使用需先配置 AccessKey。

### 配置凭证

编辑脚本顶部的 `ACCESS_KEY_ID` 和 `ACCESS_KEY_SECRET`，或通过环境变量传入：

```bash
set ALIBABA_CLOUD_ACCESS_KEY_ID=你的Key
set ALIBABA_CLOUD_ACCESS_KEY_SECRET=你的Secret
```

### 单张图片

```bash
python scripts/aliyun_seg.py 图片.jpg                     # 默认商品分割，白底输出
python scripts/aliyun_seg.py 照片.png -m body              # 人体分割
python scripts/aliyun_seg.py 商品.jpg -f mask              # 透明背景PNG
python scripts/aliyun_seg.py 商品.jpg -f crop              # 裁剪到主体区域
python scripts/aliyun_seg.py 图片.jpg -o 结果.png          # 指定输出路径
```

### 批量处理

```bash
python scripts/aliyun_seg.py ./图片目录 -m commodity       # 批量商品分割
python scripts/aliyun_seg.py ./图片目录 -o ./输出目录       # 指定输出目录
```

### 查看支持的模型

```bash
python scripts/aliyun_seg.py --list-models
```

## 支持的模型

| 模型 | 说明 | 支持返回格式 |
|------|------|-------------|
| commodity | 商品分割（白底图首选） | whiteBK, mask, crop |
| common | 通用分割 | whiteBK, mask, crop |
| body | 人体分割 | whiteBK, mask, crop |
| food | 食品分割 | whiteBK, mask, crop |
| animal | 动物分割 | whiteBK, mask, crop |
| hd_common | 高清通用分割 | 仅返回分割结果图 |
| cloth | 服饰分割 | 仅返回分割结果图 |
| logo | Logo分割 | 仅返回分割结果图 |
| vehicle | 车辆分割 | 仅返回分割结果图 |
| sky | 天空分割 | 仅返回分割结果图 |

## 返回格式

- `whiteBK` — 白色背景（默认）
- `mask` — 透明背景 PNG
- `crop` — 裁剪到主体边界框

## 注意事项

- 图片需 Base64 编码后通过 API 传输，单张不超过限制
- 凭证硬编码在脚本中，生产环境建议改用环境变量
- 支持 PNG、JPG、JPEG、WebP、BMP 格式
