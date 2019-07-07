#测试类
import requests
from API_Frame_Work.common.read_config import read_config
import os

class HttpRequest():

    def __init__(self,param,http_method):
        self.home_url =read_config().config_Http()["home_url"]
        self.register_url =  read_config().config_Http()["register_url"]
        self.param = param
        self.http_method=http_method
        self.url = self.home_url + self.register_url

    def http_request(self):
        if self.http_method.upper() == "POST":
            try:
                res = requests.post(self.url,self.param)
                print("Failed")
            except Exception as e:
                raise e
        else:
            try:
                res = requests.get(self.url,self.param)
                print("Failed")
            except Exception as e:
                raise e
        return res

if __name__=='__main__':
    url1='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
    # url1='http://test.lemonban.com/futureloan/mvc/api/member/register'
    param1={"mobilephone":"13812016000","pwd":"123456"}
    # http_method = 'post'
    # res = HttpRequest(param,http_method).http_request()
    res1 = requests.post(url1,param1)
    print(res1)
    # param = {"key":'43fe516b14cd2eee8e7db8dcda379909','date':'2019-07-04'}
    # url = "http://v.juhe.cn/laohuangli/d"
    # res = requests.post(url,param)
    # print(res.json())



