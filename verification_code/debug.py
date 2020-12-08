# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/8 17:20
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : debug.py
# @Software : PyCharm
import base64

with open('123.png', 'rb') as f:
    base64_data = base64.b64encode(f.read())
    b64 = base64_data.decode()
    print(b64)

