#ddt,结合单元测试，用来拆分数据，传递参数给测试用例

# def print_msg(*args):  #*args不定长参数
#     print("收到的数据",args)#得到的数据为元祖
#     print("数据类型",type(args))
#     print("数据长度",len(args))
#
# print_msg(1,2,3,4,5,6,7)
# a=(1,2,3,4,5,6,7)
# print_msg(a)
# print_msg(*a)

import unittest
from ddt import ddt,data,unpack


# test_data = [[1,2],[3,4]]
test_data= [{'a':1,'b':2},{'a':3,'b':4}]
@ddt #@测试类  ddt专门装饰测试类
class TestMath(unittest.TestCase):

    @data(*test_data)  #data。专门用来装饰测试用例,*test_data 拆分数据
    @unittest.skip("Norun") #跳过不执行
    def test_add_1(self,item): #item接受@data传输来的数据，item作为一个字典传递
        print(item)
        #list类型数据
        # a =item[0]
        # b =item[1]
        #字典类型数据
        a =item['a']
        b =item['b']

        res = a+b
        print("a+b的和是{0}".format(res))

    @data(*test_data)
    @unpack
    #def test_add_2(self,x,y):  #传入值为dict时，传入参数需要与key值一样
    def test_add_2(self,a,b):
        res = a+b
        print("a+b的和是{0}".format(res))

if __name__ =='__main__':
    unittest.main()