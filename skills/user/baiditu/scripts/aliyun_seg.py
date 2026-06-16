# -*- coding: utf-8 -*-
"""阿里云视觉智能 — 图片主体分割 / 白底图工具

通过 `imageseg.cn-shanghai.aliyuncs.com` 的 *Advance 接口上传图片二进制，
服务端返回签名 OSS URL，脚本再下载到本地。

设计要点
========
1. 使用 `*AdvanceRequest.image_urlobject` (BinaryIO) 上传，避免 `image_url`
   字段只接受上海 OSS 公网 URL 的限制。
2. 自动用 Pillow 把最长边缩到 2000px 以内，规避 `InvalidFile.Resolution`
   (接口硬性限制 ≤ 2000×2000)。
3. 单文件 / 目录的默认输出都在源同目录下创建 `白底图` 子目录，可用 `-o` 覆盖。
4. 10 种分割模型走统一调度：类名 `SegmentXxxAdvanceRequest`、
   方法名 `client.segment_xxx_advance(...)`。
5. 凭证优先读环境变量，未设置时回落到内置占位（生产环境务必用环境变量）。
"""

import io
import os
import sys
import argparse
import urllib.request
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # Pillow 缺失时降级：直接上传原文件
    Image = None

from alibabacloud_imageseg20191230.client import Client as ImageSegClient
from alibabacloud_imageseg20191230 import models as image_seg_models
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models


# ========== 配置 ==========
ACCESS_KEY_ID = os.environ.get(
    "ALIBABA_CLOUD_ACCESS_KEY_ID", "LTAI5t64wtNMTo7dBXkbmbFy"
)
ACCESS_KEY_SECRET = os.environ.get(
    "ALIBABA_CLOUD_ACCESS_KEY_SECRET", "HWyDK1C8LgTnpK1dcbXGIIZR7AoUC5"
)
REGION = os.environ.get("ALIBABA_CLOUD_REGION", "cn-shanghai")
ENDPOINT = "imageseg.cn-shanghai.aliyuncs.com"

# 阿里云图片分割接口长边像素上限
MAX_LONG_EDGE = 2000
DEFAULT_JPEG_QUALITY = 92

# 子目录名：默认在源目录/父目录下创建该目录保存白底图
DEFAULT_OUT_SUBDIR = "白底图"

# 模型配置：(类名前缀, 描述, 是否支持 return_form)
MODELS = {
    "commodity": ("SegmentCommodity",     "商品分割（白底图首选）", True),
    "common":    ("SegmentCommonImage",   "通用分割",              True),
    "body":      ("SegmentBody",          "人体分割",              True),
    "food":      ("SegmentFood",          "食品分割",              True),
    "animal":    ("SegmentAnimal",        "动物分割",              True),
    "hd_common": ("SegmentHDCommonImage", "高清通用分割",          False),
    "cloth":     ("SegmentCloth",         "服饰分割",              False),
    "logo":      ("SegmentLogo",          "Logo 分割",            False),
    "vehicle":   ("SegmentVehicle",       "车辆分割",              False),
    "sky":       ("SegmentSky",           "天空分割",              False),
}
RETURN_FORMS = ["whiteBK", "mask", "crop"]


def _to_snake(name: str) -> str:
    """SegmentCommodity -> segment_commodity；SegmentHDCommonImage -> segment_hdcommon_image。"""
    out = []
    for i, ch in enumerate(name):
        if ch.isupper() and i > 0 and not name[i - 1].isupper():
            out.append("_")
        out.append(ch.lower())
    return "".join(out)


def create_client() -> ImageSegClient:
    config = open_api_models.Config(
        access_key_id=ACCESS_KEY_ID,
        access_key_secret=ACCESS_KEY_SECRET,
        region_id=REGION,
    )
    config.endpoint = ENDPOINT
    return ImageSegClient(config)


def _prepare_upload(image_path: str):
    """读取图片，超 2000px 自动缩放，返回 (fileobj, ext, original_size)。

    - 不超限时直接返回原文件句柄，零拷贝；
    - 缩放后写到 BytesIO，统一用 JPEG 编码（白底场景无损画质）。
    """
    if Image is None:
        ext = Path(image_path).suffix.lstrip(".").lower() or "jpg"
        return open(image_path, "rb"), ext, None

    with Image.open(image_path) as im:
        orig_size = im.size
        longest = max(im.size)
        if longest <= MAX_LONG_EDGE:
            ext = (im.format or "JPEG").lower()
            ext = "jpg" if ext == "jpeg" else ext
            return open(image_path, "rb"), ext, orig_size

        scale = MAX_LONG_EDGE / float(longest)
        new_size = (int(im.size[0] * scale), int(im.size[1] * scale))
        if im.mode in ("RGBA", "P", "LA"):
            im2 = im.convert("RGBA")
        else:
            im2 = im.convert("RGB")
        im2 = im2.resize(new_size, Image.LANCZOS)

        buf = io.BytesIO()
        if im2.mode == "RGBA":
            im2.save(buf, format="PNG", optimize=True)
            ext = "png"
        else:
            im2 = im2.convert("RGB")
            im2.save(buf, format="JPEG", quality=DEFAULT_JPEG_QUALITY, optimize=True)
            ext = "jpg"
        buf.seek(0)
        return buf, ext, orig_size


def _download(url: str, dest: str, retries: int = 3) -> str:
    """下载签名 OSS URL 到本地，带有限重试。"""
    last_err = None
    for _ in range(retries):
        try:
            urllib.request.urlretrieve(url, dest)
            return dest
        except Exception as e:  # noqa: BLE001
            last_err = e
    raise RuntimeError(f"下载结果失败（已重试 {retries} 次）: {last_err}")


def _close_quietly(obj):
    try:
        obj.close()
    except Exception:  # noqa: BLE001
        pass


def segment_one(client, image_path, model="commodity", return_form="whiteBK"):
    """调用 *Advance 接口，返回 (result_url, ext, original_size)。"""
    runtime = util_models.RuntimeOptions(read_timeout=60000, connect_timeout=20000)
    base_name, _, supports_form = MODELS[model]

    req_cls = getattr(image_seg_models, f"{base_name}AdvanceRequest")
    method = getattr(client, f"{_to_snake(base_name)}_advance")

    fileobj, ext, orig_size = _prepare_upload(image_path)
    try:
        if supports_form:
            req = req_cls(image_urlobject=fileobj, return_form=return_form)
        else:
            req = req_cls(image_urlobject=fileobj)
        resp = method(req, runtime)
    finally:
        _close_quietly(fileobj)

    result_url = resp.body.data.image_url
    if not result_url:
        raise RuntimeError(f"API 未返回结果 URL（model={model}）")
    return result_url, ext, orig_size


def default_output_dir(input_path: str) -> Path:
    """根据输入路径推算默认输出目录：源同级的「白底图」子目录。"""
    p = Path(input_path)
    if p.is_dir():
        return p / DEFAULT_OUT_SUBDIR
    return p.parent / DEFAULT_OUT_SUBDIR


def _output_ext_for(return_form: str, in_ext: str) -> str:
    """根据返回格式推断输出扩展名：mask → png；其他跟随输入。"""
    if return_form == "mask":
        return ".png"
    return in_ext.lower() if in_ext.lower() in {".jpg", ".jpeg", ".png", ".webp", ".bmp"} else ".jpg"


def process_one(client, image_path: str, output_path: str, model: str, return_form: str):
    result_url, _, orig_size = segment_one(client, image_path, model, return_form)
    if orig_size and max(orig_size) > MAX_LONG_EDGE:
        print(
            f"  · 缩放上传（原图 {orig_size[0]}x{orig_size[1]} → 最长边 {MAX_LONG_EDGE}px）"
        )
    _download(result_url, output_path)
    return output_path


def batch_process(client, input_dir: str, output_dir: str, model: str, return_form: str):
    exts = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
    input_dir_p = Path(input_dir)
    files = sorted(f for f in os.listdir(input_dir) if (input_dir_p / f).suffix.lower() in exts)
    if not files:
        print(f"目录 {input_dir} 中没有找到图片文件")
        return 0, 0

    output_dir_p = Path(output_dir)
    output_dir_p.mkdir(parents=True, exist_ok=True)
    print(
        f"找到 {len(files)} 张图片，模型: {model}，返回: {return_form}，输出: {output_dir_p}"
    )
    ok = fail = 0
    for i, fname in enumerate(files, 1):
        in_path = input_dir_p / fname
        out_ext = _output_ext_for(return_form, in_path.suffix)
        out_path = output_dir_p / (in_path.stem + out_ext)
        print(f"[{i}/{len(files)}] {fname} ... ", end="", flush=True)
        try:
            process_one(client, str(in_path), str(out_path), model, return_form)
            print(f"OK -> {out_path.name}")
            ok += 1
        except Exception as e:  # noqa: BLE001
            print(f"FAIL: {e}")
            fail += 1
    return ok, fail


def main():
    parser = argparse.ArgumentParser(
        description=(
            "阿里云视觉智能图片分割 — 输出白底图 / 透明 PNG / 裁剪图。\n"
            "默认行为：若输入是目录，在其下创建「白底图」子目录；\n"
            "         若输入是文件，在文件同目录下创建「白底图」子目录。\n"
            "可用 -o 覆盖输出位置。"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("input", nargs="?", default=None,
                        help="输入图片文件或目录")
    parser.add_argument("-o", "--output", default=None,
                        help="输出文件路径或目录；不传则按默认行为在源目录下创建「白底图」")
    parser.add_argument("-m", "--model", default="commodity", choices=list(MODELS.keys()),
                        help="分割模型（默认: commodity 商品分割）")
    parser.add_argument("-f", "--form", default="whiteBK", choices=RETURN_FORMS,
                        help="返回格式: whiteBK(白底) / mask(透明) / crop(裁剪)。默认 whiteBK")
    parser.add_argument("--list-models", action="store_true",
                        help="列出所有支持的模型与返回格式")
    args = parser.parse_args()

    if args.list_models:
        print("支持的模型:")
        for k, (_, desc, supports_form) in MODELS.items():
            forms = "whiteBK / mask / crop" if supports_form else "仅返回分割结果图"
            print(f"  {k:<11s} {desc:<14s}  返回: {forms}")
        return

    if not args.input:
        parser.error(
            "请指定输入图片路径或目录（或 --list-models 查看支持的模型）"
        )

    model = args.model
    return_form = args.form
    if not MODELS[model][2] and return_form != "whiteBK":
        print(f"提示: 模型 {model} 不支持自定义返回格式，将返回默认分割结果图")

    client = create_client()

    if os.path.isdir(args.input):
        output_dir = args.output or str(default_output_dir(args.input))
        ok, fail = batch_process(client, args.input, output_dir, model, return_form)
        print(f"\n完成: 成功 {ok} 张, 失败 {fail} 张, 输出目录: {output_dir}")
        return

    in_path = Path(args.input)
    if args.output:
        out_path = Path(args.output)
        if out_path.is_dir() or str(out_path).endswith(("/", "\\")):
            out_path = out_path / (
                in_path.stem + _output_ext_for(return_form, in_path.suffix)
            )
    else:
        out_dir = default_output_dir(in_path)
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / (in_path.stem + _output_ext_for(return_form, in_path.suffix))

    print(f"处理: {args.input} (模型: {model}, 返回: {return_form})")
    process_one(client, args.input, str(out_path), model, return_form)
    print(f"完成 -> {out_path}")


if __name__ == "__main__":
    main()