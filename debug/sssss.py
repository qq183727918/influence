# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/4 15:10
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : sssss.py
# @Software : PyCharm
import base64
import json
import requests

def base64_api(uname, pwd,  img):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


if __name__ == "__main__":
    img_path = r"D:\C-File\C-desktop\image\123.png"
    result = base64_api(uname='liuxiaoqiang', pwd='lxqiang95', img=img_path)
    print(result)
