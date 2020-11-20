# !/bin/python3
# -*- coding:utf-8 -*-

import logging
import os

import django
from django.conf import settings

from Common.LogHandler import setup_logger


def init_superuser():
    '''
    创建管理员用户
    :return:
    '''
    setup_logger()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ImageRecognition.settings")
    django.setup()
    from django.contrib.auth.models import User
    username = settings.SUPERUSER_NAME
    password = settings.SUPERUSER_PASSWORD
    email = settings.SUPERUSER_EMAIL
    user = User.objects.filter(username=username).first()
    if user:
        logging.warning('User [%s] already exist' % username)
    else:
        User.objects.create_superuser(
            username=username,
            password=password,
            email=email
        )
        logging.info('create superuser ok')


if __name__ == '__main__':
    init_superuser()
