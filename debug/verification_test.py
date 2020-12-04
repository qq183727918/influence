# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/4 17:01
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : verification_test.py
# @Software : PyCharm
# from PIL import Image
#
# #使用路径导入图片
# imgName = '1.png'
# im = Image.open(imgName)
# #使用 byte 流导入图片
# # im = Image.open(io.BytesIO(b))
# # 转化到灰度图
# imgry = im.convert('L')
# # 保存图像
# imgry.save('gray-' + imgName)

# 二值化，采用阈值分割法，threshold为分割点
# threshold = 140
# table = []
# for j in range(256):
#     if j < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# out = imgry.point(table, '1')
# out.save('b' + imgName)

import pytesseract
#  识别
text = pytesseract.image_to_string('1.png')
print(f"识别结果：{text}")
