# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/7 17:17
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : code_test.py
# @Software : PyCharm
# from PIL import Image,ImageEnhance,ImageFilter
#
# image = Image.convert('L')
# threshold = 80
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# image = image.point(table, '1')
# image.show()
from PIL import Image
# import tesseract


class demo():

    def __init__(self, path):
        self.image = Image.open(path)
        self.image = self.image.convert('L')

    def test(self):
        threshold = 127
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        self.image = self.image.point(table, '1')
        self.img_array = self.image.load()
        width = self.image.size[0]
        height = self.image.size[1]
        for i in range(0, 1000):
            for x in range(1, width - 1):
                for y in range(1, height - 1):
                    count = 0
                    if self.img_array[x, y] == self.img_array[x - 1, y + 1]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x, y + 1]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x + 1, y + 1]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x - 1, y]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x + 1, y]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x - 1, y - 1]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x, y - 1]:
                        count += 1
                    if self.img_array[x, y] == self.img_array[x + 1, y - 1]:
                        count += 1
                    if count <= 3 and count > 0:
                        self.img_array[x, y] = 1
        self.image.show()

# demo('1213.png').test()
import pytesseract
from PIL import Image

image = Image.open('1.png')
result = pytesseract.image_to_data(image)
print(result)
