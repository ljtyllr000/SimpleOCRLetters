# !/bin/python3
# -*- coding:utf-8 -*-

import logging

import pymysql
from django.conf import settings

from Common.LogHandler import setup_logger


def create_db():
    setup_logger()
    db_name = settings.DATABASES.get('default').get('NAME')
    db_host = settings.DATABASES.get('default').get('HOST')
    db_user = settings.DATABASES.get('default').get('USER')
    db_pwd = settings.DATABASES.get('default').get('PASSWORD')

    try:
        conn = pymysql.connect(db_host, db_user, db_pwd, charset='utf8')
        cursor = conn.cursor()
        cursor.execute('SHOW DATABASES')
        db_exist = False
        for ele in cursor.fetchall():
            if ele[0] == db_name:
                db_exist = True
                break
        if not db_exist:
            cursor.execute('CREATE DATABASE %s' % db_name)
            logging.info('success to create db')
        else:
            logging.info('db already exist')
        conn.close()
    except Exception as e:
        logging.error(str(e))


if __name__ == '__main__':
    create_db()
