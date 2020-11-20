# !/usr/bin/python3
# -*- coding:utf-8 -*-

from PIL import Image

import pytesseract


def recognize_str(image_path):
    """
    识别图片路径中图片中的英文字符
    :param image_path: 图片路径
    :return:
    """
    images = Image.open(image_path)
    image_str = pytesseract.image_to_string(images)
    return image_str
