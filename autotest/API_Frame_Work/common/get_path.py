import os

class Get_Path():

    def __init__(self):
        #获取当前的项目根目录
        self.base_path = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))

    def get_base_path(self):
        base_path = self.base_path
        return base_path

    def get_config_path(self,):
        config_path = os.path.join(self.base_path,"conf")
        return config_path

    def get_test_data_path(self):
        test_data_path = os.path.join(self.base_path,"test_data")
        return test_data_path

    def get_test_result_path(self):
        test_result_path = os.path.join(self.base_path,"test_result")
        return test_result_path

if __name__ =='__main__':
    getpath = Get_Path()
    print(getpath.get_base_path())
    print(getpath.get_config_path())
    print(getpath.get_test_data_path())




