from configparser import ConfigParser
import os
from API_Frame_Work.common.get_path import Get_Path

class read_config():

    def __init__(self):
        self.config_path = Get_Path().get_config_path()
        self.config_path= os.path.join(self.config_path,"config.config")
        self.cf = ConfigParser()
        read_config_case = self.cf.read(self.config_path)

    #获取到case的配置
    #all_run on 跑全部case 否则跑test_case_id配置的case
    def config_case(self):
        all_run = self.cf.get("CaseConfig","all_run")
        test_case_id = eval(self.cf.get("CaseConfig","test_case_id"))
        # return_data = {}
        return_data = {'all_run':all_run,'test_case_id':test_case_id}
        # print(return_data)
        return return_data

    def config_Http(self):
        home_url = eval(self.cf.get("HttpConfig","home_url"))
        register_url = eval(self.cf.get("HttpConfig","register_url"))
        return_data = {"home_url":home_url,"register_url":register_url}
        return return_data

    def config_Email(self):
        pass

    def config_DB(self):
        pass

    #测试用例数据配置
    def config_Test_Data(self):
        file_name = eval(self.cf.get("Test_Data","file_name"))
        sheet_name = eval(self.cf.get("Test_Data","sheet_name"))
        return_data={"file_name":file_name,"sheet_name":sheet_name}
        return return_data

    #测试结果配置
    def config_Test_Result(self):
        file_name= eval(self.cf.get("Test_Result","file_name"))
        sheet_name= eval(self.cf.get("Test_Result","sheet_name"))
        return_data={"file_name":file_name,"sheet_name":sheet_name}
        return return_data


if __name__ =="__main__":
    rd= read_config()
    data1 = rd.config_case()
    data2 = rd.config_Http()
    data3 = rd.config_Test_Data()
    data4 = rd.config_Test_Result()
    print(type(data1['all_run']))
    print(data1)
    print(data2)
    print(data3)
    print(data4)
    url = data2["home_url"]+data2["register_url"]
    print(url)



