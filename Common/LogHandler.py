# !/usr/bin/python3
# -*- coding:utf-8 -*-

import os
import logging

import django
from django.conf import settings


def setup_logger():
    """"
    配置日志相关
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ImageRecognition.settings')
    django.setup()

    log_format = logging.Formatter(fmt='[%(asctime)s][%(pathname)s][%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger('')
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        log_level = settings.LOG_OUTPUT_LEVEL
        log_output = logging.StreamHandler()
        log_output.setLevel(log_level)
        log_output.setFormatter(log_format)
        logger.addHandler(log_output)

        log_level = settings.LOG_FILE_LEVEL
        log_file_path = settings.LOG_FILE
        log_dir = os.path.dirname(log_file_path)
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        file_log = logging.FileHandler(log_file_path)
        file_log.setLevel(log_level)
        file_log.setFormatter(log_format)
        logger.addHandler(file_log)
