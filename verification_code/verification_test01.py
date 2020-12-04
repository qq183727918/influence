# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/4 16:49
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : verification_test01.py
# @Software : PyCharm
from PIL import Image
import pytesseract

def recognize_captcha(img_path):
    im = Image.open(img_path)
    # threshold = 140
    # table = []
    # for i in range(256):
    #     if i < threshold:
    #         table.append(0)
    #     else:
    #         table.append(1)
    #
    # out = im.point(table, '1')
    num = pytesseract.image_to_string(im)
    return num


if __name__ == '__main__':
    for i in range(1, 12):
        img_path = str(i) + ".jpeg"
        res = recognize_captcha(img_path)
        strs = res.split("\n")
        if len(strs) >=1:
            print (strs[0])
