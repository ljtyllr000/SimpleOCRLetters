# !/usr/bin/python3
# -*- coding:utf-8 -*-

import os


def get_project_dir():
    """
    项目根目录
    :return:
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
