# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/30 13:05
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : HttpJson.py
# @Software : PyCharm
import requests
import pprint
import unittest
from ddt import ddt, data, file_data


@ddt
class MyTesting(unittest.TestCase):
    def setUp(self):
        print('this is the setUp')

    @file_data('./HttpJson.json')
    def test_1(self, url, params):
        print(url)
        respon = requests.get(url, params)

        re = respon.json()

        pprint.pprint(re)

    def tearDown(self):
        print('this is tearDown')


if __name__ == '__main__':
    import unittest
    import HTMLrunnerTest

    filename = 'D:\HttpRunner\Reports\HttpYmal_test.html'  # 测试报告的存放路径及文件名
    fp = open(filename, 'wb')  # 创测试报告html文件，此时还是个空文件
    suite = unittest.defaultTestLoader.discover('../HttpYaml/', pattern='*.py')

    runner = HTMLrunnerTest.HTMLTestRunner(stream=fp, title='接口测试报告', description='测试结果如下: ')
    result = runner.run(suite)  # 执行测试
    fp.close()
