import configparser
#实例化
class ReadConfig():

    def read_config(self,file_path,section,option):
        cf = configparser.ConfigParser()
        #调用read函数，打开文件
        cf.read(file_path)
        #读取数据，读取到的都是字符串类型
        #使用eval，将data变为原本的类型，即换成list
        value = cf.get(section,option)
        #eval(data),将data数据转换成python能够识别的数据类型
        #
        return value


if __name__ =='__main__':
    value = ReadConfig().read_config("case.config",'FLAG','cse_id_list')
    print(value)