# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/30 11:31
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : HttpYaml.py
# @Software : PyCharm
import requests
import pprint
import unittest


class MyTesting(unittest.TestCase):
    def setUp(self):
        print('this is the setUp')


    def test01(self):
        # print(kwargs.get('url'))
        pass
        # respon = requests.get(url, params)
        #
        # re = respon.json()
        #
        # pprint.pprint(re)

    def tearDown(self):
        print('this is tearDown')

if __name__ == '__main__':

    pass
