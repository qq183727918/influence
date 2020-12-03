# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/2 19:34
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : __init__.py.py
# @Software : PyCharm
import requests
import pprint

def token_test():
    ak = "06F8XRdDMg9Fk3zeXDvNGRDf"
    sk = "AvynGXGhYd5EOZoFxssnZOgiKNB8i4UE"
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={ak}&client_secret={sk}'
    response = requests.get(host)
    if response:
        pprint.pprint(response.json())
