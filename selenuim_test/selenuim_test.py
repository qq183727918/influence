# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/8 11:20
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : selenuim_test.py
# @Software : PyCharm
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

admin_url = 'http://47.116.74.54/#/appointment/appointment'

driver.get(admin_url)

print(driver.get_cookies())
dict_cookies1 = {"domain": "47.116.74.54", "name": "requestTime", "path": "/", "value": "1607413844726"}
dict_cookies2 = {"domain": "47.116.74.54", "name": "expiresIn", "path": "/", "value": "3585058"}
dict_cookies3 = {"domain": "47.116.74.54", "name": "isSupperTenant", "path": "/", "value": "true"}
dict_cookies4 = {"domain": "47.116.74.54", "name": "refresh-token", "path": "/",
                 "value": "a27a8c72-ca97-45cf-a9fd-45a0f52e3d37"}
dict_cookies5 = {"domain": "47.116.74.54", "name": "Authorization", "path": "/",
                 "value": "52a5a0a5-3771-4aa3-ac33-8aa00dd41f95"}
dict_cookies6 = {"domain": "47.116.74.54", "name": "SESSION", "path": "/", "sameSite": "Lax",
                 "value": "YjM0NGVjNjktNTgxYi00OGNkLTk3NWItMjM5YWM5NTFhODg2"}

driver.add_cookie(dict_cookies1)
driver.add_cookie(dict_cookies2)
driver.add_cookie(dict_cookies3)
driver.add_cookie(dict_cookies4)
driver.add_cookie(dict_cookies5)
driver.add_cookie(dict_cookies6)

print(driver.get_cookies())
# driver.close()
driver.refresh()
url = 'http://47.116.74.54/#/appointment/appointment'
driver.get(url)

sleep(10)
driver.quit()
'Cookie: isSupperTenant=true; ' \
'SESSION=ODRlYzkwODYtZDgzZC00Y2I4LTg1MDctM2RkNWQ1Y2U3ODA1; ' \
'expiresIn=3599089; ' \
'requestTime=1607415445043'


'Cookie: isSupperTenant=true; ' \
'SESSION=NmYwNjdkYTEtYjc0OC00MThhLTllOWYtMzgyZDgxZjdjODhk; ' \
'Authorization=20d58d59-34d6-4585-8c89-a47745273b04; ' \
'refresh-token=bf906db5-7a5e-44f7-83d3-62cc6b738434; ' \
'expiresIn=3599999; ' \
'requestTime=1607415469419'
