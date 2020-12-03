# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/2 17:37
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : verificationCode.py
# @Software : PyCharm
import sys
import uuid
import requests
import base64
import hashlib

from imp import reload


import time

reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/ocrapi'
APP_KEY = '01f977142396c328'
APP_SECRET = 'UEVZofhmpuTVnkx3U1vdnVOgPSSiqkPV'


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect():
    f = open(r'D:\C-File\C-desktop\image\123.png', 'rb')  # 二进制方式打开图文件
    q = base64.b64encode(f.read()).decode('utf-8')  # 读取文件内容，转换为base64编码
    f.close()

    data = {}
    data['detectType'] = '10012'
    data['imageType'] = '1'
    data['langType'] = 'en'
    data['img'] = q
    data['docType'] = 'json'
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    print(response.content)


if __name__ == '__main__':
    connect()
