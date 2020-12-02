# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/23 19:31
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : HttpLocust.py
# @Software : PyCharm
from locust import HttpLocust, task

class Quickstart(HttpLocust):
    min_wait = 100  # 最小等待时间(ms)，模拟用户在执行每个任务之间等待的最小时间
    max_wait = 500  # 最大等待时长(ms)，模拟用户在执行每个任务之间等待的最大时长
    host = 'https://baidu.com'  # 访问的域名

    def on_start(self):
        #开始任务
        print("start working")

    # 任务target，用@task标记
    @task
    def test(self):
        self.client.get('/')
