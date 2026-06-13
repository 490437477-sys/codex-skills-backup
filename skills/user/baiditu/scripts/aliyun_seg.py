# -*- coding: utf-8 -*-
"""阿里云图片分割工具 - 支持商品分割、通用分割、人体分割等"""

import os
import sys
import base64
import argparse
from alibabacloud_imageseg20191230.client import Client as ImageSegClient
from alibabacloud_imageseg20191230 import models as image_seg_models
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util import models as util_models

# ========== 配置 ==========
ACCESS_KEY_ID = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_ID", "LTAI5t64wtNMTo7dBXkbmbFy")
ACCESS_KEY_SECRET = os.environ.get("ALIBABA_CLOUD_ACCESS_KEY_SECRET", "HWyDK1C8LgTnpK1dcbXGIIZR7AoUC5")
REGION = os.environ.get("ALIBABA_CLOUD_REGION", "cn-shanghai")

# 支持的模型及其说明
MODELS = {
    "commodity":  ("SegmentCommodity",   "商品分割（适合白底图）"),
    "common":     ("SegmentCommonImage",  "通用分割"),
    "body":       ("SegmentBody",         "人体分割"),
    "food":       ("SegmentFood",         "食品分割"),
    "hd_common":  ("SegmentHDCommonImage","高清通用分割"),
    "cloth":      ("SegmentCloth",        "服饰分割"),
    "logo":       ("SegmentLogo",         "Logo分割"),
    "vehicle":    ("SegmentVehicle",      "车辆分割"),
    "animal":     ("SegmentAnimal",       "动物分割"),
    "sky":        ("SegmentSky",          "天空分割"),
}


def create_client():
    config = open_api_models.Config(
        access_key_id=ACCESS_KEY_ID,
        access_key_secret=ACCESS_KEY_SECRET,
        region_id=REGION,
    )
    config.endpoint = "imageseg.cn-shanghai.aliyuncs.com"
    return ImageSegClient(config)


def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def save_base64_image(b64_str, output_path):
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(b64_str))


def segment_image(client, image_path, model="commodity", return_form="whiteBK"):
    img_base64 = image_to_base64(image_path)
    runtime = util_models.RuntimeOptions()

    if model == "commodity":
        req = image_seg_models.SegmentCommodityRequest(image_url=img_base64, return_form=return_form)
        resp = client.segment_commodity_with_options(req, runtime)
    elif model == "common":
        req = image_seg_models.SegmentCommonImageRequest(image_url=img_base64, return_form=return_form)
        resp = client.segment_common_image_with_options(req, runtime)
    elif model == "body":
        req = image_seg_models.SegmentBodyRequest(image_url=img_base64, return_form=return_form)
        resp = client.segment_body_with_options(req, runtime)
    elif model == "food":
        req = image_seg_models.SegmentFoodRequest(image_url=img_base64, return_form=return_form)
        resp = client.segment_food_with_options(req, runtime)
    elif model == "hd_common":
        req = image_seg_models.SegmentHDCommonImageRequest(image_url=img_base64)
        resp = client.segment_hdcommon_image_with_options(req, runtime)
    elif model == "cloth":
        req = image_seg_models.SegmentClothRequest(image_url=img_base64)
        resp = client.segment_cloth_with_options(req, runtime)
    elif model == "logo":
        req = image_seg_models.SegmentLogoRequest(image_url=img_base64)
        resp = client.segment_logo_with_options(req, runtime)
    elif model == "vehicle":
        req = image_seg_models.SegmentVehicleRequest(image_url=img_base64)
        resp = client.segment_vehicle_with_options(req, runtime)
    elif model == "animal":
        req = image_seg_models.SegmentAnimalRequest(image_url=img_base64, return_form=return_form)
        resp = client.segment_animal_with_options(req, runtime)
    elif model == "sky":
        req = image_seg_models.SegmentSkyRequest(image_url=img_base64)
        resp = client.segment_sky_with_options(req, runtime)
    else:
        raise ValueError(f"不支持的模型: {model}，可选: {list(MODELS.keys())}")

    return resp.body.data.image_url


def batch_segment(client, input_dir, output_dir, model="commodity", return_form="whiteBK"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    exts = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
    files = [f for f in os.listdir(input_dir) if os.path.splitext(f)[1].lower() in exts]

    if not files:
        print(f"目录 {input_dir} 中没有找到图片文件")
        return

    print(f"找到 {len(files)} 张图片，使用模型: {model}")
    for i, f in enumerate(files, 1):
        input_path = os.path.join(input_dir, f)
        name, _ = os.path.splitext(f)
        output_path = os.path.join(output_dir, f"{name}_seg.png")

        print(f"[{i}/{len(files)}] 处理: {f} ... ", end="", flush=True)
        try:
            result = segment_image(client, input_path, model, return_form)
            save_base64_image(result, output_path)
            print(f"OK -> {output_path}")
        except Exception as e:
            print(f"FAIL: {e}")


def main():
    parser = argparse.ArgumentParser(description="阿里云图片分割工具")
    parser.add_argument("input", nargs="?", default=None, help="输入图片路径或目录")
    parser.add_argument("-o", "--output", default=None, help="输出路径（默认: 输入文件名_seg.png）")
    parser.add_argument("-m", "--model", default="commodity",
                        choices=list(MODELS.keys()),
                        help="分割模型（默认: commodity 商品分割）")
    parser.add_argument("-f", "--form", default="whiteBK",
                        choices=["whiteBK", "mask", "crop"],
                        help="返回格式: whiteBK(白底), mask(透明), crop(裁剪)")
    parser.add_argument("--list-models", action="store_true", help="列出所有支持的模型")

    args = parser.parse_args()

    if args.list_models:
        print("支持的模型:")
        for k, (api, desc) in MODELS.items():
            print(f"  {k:12s} -> {api:24s} {desc}")
        return

    if not args.input:
        parser.error("请指定输入图片路径或目录")

    client = create_client()

    if os.path.isdir(args.input):
        output_dir = args.output or os.path.join(args.input, "output")
        batch_segment(client, args.input, output_dir, args.model, args.form)
    else:
        output = args.output or f"{os.path.splitext(args.input)[0]}_seg.png"
        print(f"处理: {args.input} (模型: {args.model})")
        result = segment_image(client, args.input, args.model, args.form)
        save_base64_image(result, output)
        print(f"完成: {output}")


if __name__ == "__main__":
    main()
