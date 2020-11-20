# !/usr/bin/python3
# -*- coding:utf-8 -*-
import logging
import os
import time

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from Common.DataHandler import str_encryption, deal_recognition_res
from Common.LogHandler import setup_logger
from Common.PathHandler import get_project_dir
from app01 import models
from app01.Functions.Image2String import recognize_str

setup_logger()


@csrf_protect
def recognize_image(request):
    data = {'status': '200', 'msg': ''}
    if request.method == 'GET':
        return render(request, 'image.html', locals())

    file = request.FILES.get('image')
    if file:

        file_size = file.size
        if file_size > 5 * 1024 * 1024:
            data['status'] = '401'
            data['msg'] = '图片文件过不能大于5M'
            logging.warning('Fail to create task, the file too big')
            return JsonResponse(data)

        if file_size == 0:
            data['status'] = '402'
            data['msg'] = '图片文件是空文件'
            logging.warning('Fail to create scan task, the file is empty')
            return JsonResponse(data)

        # 保存上传图片
        file_name_suffix = file.name.split('.')[-1]
        if file_name_suffix not in ['jpg', 'png']:
            data['status'] = '403'
            data['msg'] = '请上传jpg/png格式图片'
            logging.warning('Fail to create scan task, not picture')
            return JsonResponse(data)

        save_file_name = str_encryption(file.name) + '.' + file_name_suffix
        file_path = os.path.join(get_project_dir(), 'files', save_file_name)
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))
        with open(file_path, 'wb') as f:
            for line in file.chunks():
                f.write(line)

        # 识别字符
        image_str = recognize_str(file_path)

        # 处理识别结果
        recognize_result = deal_recognition_res(image_str)
        if recognize_result:
            # 保存识别结果
            models.RecognitionRecoder.objects.get_or_create(file_name=save_file_name, upload_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), image_str=recognize_result)
            data['msg'] = recognize_result
        else:
            data['status'] = '405'
            data['msg'] = '未能识别出字符信息'
            logging.warning('Fail to recognition useful info')
    else:
        data['status'] = '404'
        data['msg'] = '未上传文件'
        logging.error('Not upload picture')
    return JsonResponse(data)
