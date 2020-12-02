# _*_ coding: UTF-8 _*_
# @Time     : 2020/11/24 10:41
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : HttpRunner_test.py
# @Software : PyCharm
import yaml
import os

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlPath = os.path.join(curPath, "HttpRunner_test.yaml")

# open方法打开直接读出来
f = open(yamlPath, 'r', encoding='utf-8')
cfg = f.read()
print(type(cfg))  # 读出来是字符串
print(cfg)

d = yaml.load(cfg)  # 用load方法转字典
print(d)
print(type(d))
