# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/20 14:31
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : Httpinfluence.py
# @Software : PyCharm
import requests
import pprint
import unittest
import HTMLrunnerTest

class Locust(unittest.TestCase):
    def setUp(self) -> None:
        '''接口测试报告测试'''

    # def test_table(self):
    #     '''接口测试报告测试'''
    #
    #     self.url = 'https://gateway.dev.vevor.net/scp-procurement-service/controller-procurementPaymentOpsService/front/getList'
    #
    #     self.parmas = {
    #         'paymentOrderSn': 'YFK202011090075',
    #         'type': 1,
    #         'currentPage': 1,
    #         'pageSize': 10
    #     }
    #
    #     self.resop = requests.get(self.url,self.parmas)
    #
    #     self.re = self.resop.json()
    #
    #     pprint.pprint(self.re)

    def test_move(self):
        '''接口测试报告测试'''

        self.url = 'https://gateway.dev.vevor.net/scp-procurement-service/controller-procurementPaymentOpsService/front/getList'

        self.parmas = {
            'paymentOrderSn': 'YFK202011090074',
            'type': 1,
            'currentPage': 1,
            'pageSize': 10
        }

        self.resop = requests.get(self.url,self.parmas)

        self.re = self.resop.json()

        pprint.pprint(self.re)


    def tearDown(self) -> None:
        '''接口测试报告测试'''


if __name__ == "__main__":

    filename = './influence.html'    #测试报告的存放路径及文件名
    fp = open(filename, 'wb')    # 创测试报告html文件，此时还是个空文件

    suite = unittest.TestSuite()   # 调用unittest的TestSuite(),理解为管理case的一个容器（测试套件）

    suite.addTest(Locust('test01'))  # 向测试套件中添加用例，"Influence"是上面定义的类名，"test"是用例名
    # runner = unittest.TextTestRunner()   # 执行套件中的用例
    runner = HTMLrunnerTest.HTMLTestRunner(stream=fp, title='接口测试报告', description='测试结果如下: ')
    result = runner.run(suite)   # 执行测试
    # print(result.success_count)  # 运行成功的数目
    # print(result.testsRun)  # 运行测试用例的总数
    # print(result.failure_count)  # 运行失败的数目
    fp.close()   # 关闭文件流，将HTML内容写进测试报告文件

suite = unittest.TestLoader().loadTestsFromTestCase(Locust)
unittest.TextTestRunner(verbosity=2).run(suite)
