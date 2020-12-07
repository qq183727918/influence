# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/7 17:17
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : code_test.py
# @Software : PyCharm
import os
import os.path
from PIL import Image, ImageEnhance, ImageFilter
import random

#二值化处理
#strImgPath 图片路径
def BinaryzationImg(strImgPath):
    #打开图片
    imgOriImg = Image.open(strImgPath)

    #增加对比度
    pocEnhance = ImageEnhance.Contrast(imgOriImg)
    #增加255%对比度
    imgOriImg = pocEnhance.enhance(2.55)

    #锐化
    pocEnhance = ImageEnhance.Sharpness(imgOriImg)
    #锐化200%
    imgOriImg = pocEnhance.enhance(2.0)

    #增加亮度
    pocEnhance = ImageEnhance.Brightness(imgOriImg)
    #增加200%
    imgOriImg = pocEnhance.enhance(2.0)

    #添加滤镜效果
    imgGryImg = imgOriImg.convert('L').filter(ImageFilter.DETAIL)

    #二值化处理
    imgBinImg = imgGryImg.convert('1')

    return imgBinImg

#去除噪点
def ClearNoise(imgBinImg):
    for x in range(1, (imgBinImg.size[0]-1)):
        for y in range(1,(imgBinImg.size[1] - 1)):
            #一个点为黑色，周围8个点为白色，则此点为噪点，设置为白色
            if imgBinImg.getpixel((x, y)) == 0 \
                    and imgBinImg.getpixel(((x - 1), (y + 1))) == 255 \
                    and imgBinImg.getpixel(((x - 1), y)) == 255 \
                    and imgBinImg.getpixel(((x - 1), (y - 1))) == 255 \
                    and imgBinImg.getpixel(((x + 1), (y + 1))) == 255 \
                    and imgBinImg.getpixel(((x + 1), y)) == 255 \
                    and imgBinImg.getpixel(((x + 1), (y - 1))) == 255 \
                    and imgBinImg.getpixel((x, (y + 1))) == 255 \
                    and imgBinImg.getpixel((x, (y - 1))) == 255:
                imgBinImg.putpixel([x, y], 255)

    return imgBinImg




















# # 定义常量
# APP_ID = '11352343'
# API_KEY = 'Nd5Z1NkGoLDvHwBnD2bFLpCE'
# SECRET_KEY = 'A9FsnnPj1Ys2Gof70SNgYo23hKOIK8Os'
#
# # 初始化AipFace对象
# aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#
# # 读取图片
# filePath='1.png'
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()
#
#     # 定义参数变量
# options = {
#     'detect_direction': 'true',
#     'language_type': 'CHN_ENG',
# }
#
# # 调用通用文字识别接口
# result = aipOcr.basicGeneral(get_file_content(filePath), options)
# print(result)
# words_result=result['words_result']
# for i in range(len(words_result)):
#     print(words_result[i]['words'].replace(' ','').replace('.','')) #去掉可能被识别的空格与.
