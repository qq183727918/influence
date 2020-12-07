# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/7 17:06
# @Author   : LiuXiaoQiang
# @Site     : http:www.cdtest.cn/
# @File     : images_test.py
# @Software : PyCharm
from aip import AipOcr
class baiduApi:
    def __init__(self,APP_ID,API_KEY,SECRET_KEY):
        '''
        """ 你的 APPID AK SK """
        APP_ID = '你的 App ID'
        API_KEY = '你的 Api Key'
        SECRET_KEY = '你的 Secret Key'
        '''
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


    """ 读取图片 """
    def get_file_content(self,imageFile):
        with open(imageFile, 'rb') as fp:
            return fp.read()

    def getWordFromImage(self,imageFile):
        image = self.get_file_content(imageFile)
        result = self.client.basicGeneral(image)
        print(result)

if __name__=="__main__":
    APP_ID='15307894'
    API_KEY='eT4rkU2i2X2quti4Z5kIl8dT'
    SECRET_KEY='UCo2WIQoMq12TR98Nm2N1PgfhWT47'
    obj = baiduApi(APP_ID,API_KEY,SECRET_KEY)
    imageFile='1.png'
    obj.getWordFromImage(imageFile)
