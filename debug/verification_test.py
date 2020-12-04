# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/4 17:01
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : verification_test.py
# @Software : PyCharm
from PIL import Image
# 转换灰度
#使用路径导入图片
imgName = '1.png'
im = Image.open(imgName)
#使用 byte 流导入图片
# im = Image.open(io.BytesIO(b))
# 转化到灰度图
imgry = im.convert('L')
# 保存图像
imgry.save('gray-' + imgName)

#  二值化降噪的过程
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open('gray-1.png')
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.show()
im.save('./1213.png')

