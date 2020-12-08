# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/8 11:27
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : cookies.py
# @Software : PyCharm
from selenium import webdriver
import os
import time
import json


def browser_initial():
    """"
    进行浏览器初始化
    """
    # os.chdir('E:\\pythonwork')
    driver = webdriver.Chrome()
    driver.maximize_window()
    log_url = 'http://47.116.74.54/#/appointment/appointment'
    time.sleep(3)
    cookieBefore = driver.get_cookies()
    print(cookieBefore)

    return log_url, driver


def get_cookies(log_url, driver):
    """
    获取cookies保存至本地
    """
    driver.get(log_url)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/a/button/span').click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@placeholder='请输入租户ID']").send_keys('admin')
    time.sleep(1)
    driver.find_element_by_xpath("//input[@placeholder='请输入账号']").send_keys('murphy')
    time.sleep(1)
    driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys('!sishun666')
    time.sleep(10)  # 进行扫码
    driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
    time.sleep(1)
    dictCookies = driver.get_cookies()  # 获取list的cookies
    print(dictCookies)
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存

    with open('./cookies11.txt', 'a') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')
    # driver.quit()


if __name__ == "__main__":
    tur = browser_initial()
    get_cookies(tur[0], tur[1])
