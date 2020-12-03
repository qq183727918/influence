# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/2 17:55
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : verification.py
# @Software : PyCharm
import requests
import base64
#被引用模块所在的路径
from verification.token_test import token_test

token = token_test()

print(token)
# '''
# 通用文字识别（高精度版）
# '''
#
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# # 二进制方式打开图片文件
# f = open(r'D:\C-File\C-desktop\image\123.png', 'rb')
# img = base64.b64encode(f.read())
#
# params = {"image": img}
# access_token = '[调用鉴权接口获取的token]'
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print(response.json())
