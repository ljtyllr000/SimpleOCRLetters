# !/usr/bin/python3
# -*- coding:utf-8 -*-

import hashlib

from django.conf import settings


def str_encryption(source_str):
    """
    对字符串数据进行加密
    :param source_str: 原始字符串
    :return:
    """
    md = hashlib.md5()
    md.update(source_str.encode('utf-8'))
    temp_res = md.hexdigest()
    temp_res += settings.ENCRYPTION_SALT
    md.update(temp_res.encode('utf-8'))
    encryption_res = md.hexdigest()
    return encryption_res


def deal_recognition_res(result_str):
    """
    处理识别结果
    :param result_str:
    :return:
    """
    result_dict = dict()
    if result_str:
        temp_list = result_str.split('\n')
        letter_list = [item for item in temp_list if item.strip()]
        result_dict['content'] = letter_list
    return result_dict
