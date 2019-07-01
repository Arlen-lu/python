#加载测试用例
import unittest
#导入测试报告模块
import HTMLTestRunnerNew
#加载测试类
from unittest_testcase import TestAdd
from unittest_testcase import TestSub
from unittest_testcase import Test_Add
#导入ddt的测试类
from unittest_testcase_ddt import Test_Add_ddt
#从excel中导入数据
from unittest_testcase_excel import DoExcel
from unittest_testcase_excel import GetExcel
#导入配置文件
from read_config import ReadConfig
#获取配置文件中的值
button = ReadConfig().read_config("case.config",'FLAG','button')
case_id_list = eval(ReadConfig().read_config("case.config",'FLAG','cse_id_list'))
#获取path值
excel_path = GetExcel("testdata.xlsx").Get_Excel_Path()
excel_title = "testdata"
#获取测试数据
test_data1 = DoExcel(excel_path,excel_title).do_excel1()
test_data2 = DoExcel(excel_path,excel_title).do_excel2(button,case_id_list)


print(test_data2)
#多条数据数组
test_data0 = [[0,0,0,"两个零相加"],
             [1,2,3,"两个正数相加"],
             [-1,-4,-5,"两个负数相加"],
             [1,0,4,"一正一零相加"],
             [-1,0,-4,"一负一零相加"]
             ]
#创建测试套件/测试用例的容器/集合
suit = unittest.TestSuite()

#将测试用例放入套件suit中去
#方法一
#将测试用例以实例的方式传入,addTest加入suit操作
# suit.addTest(TestAdd("test_add_two_zero"))
# #具体到对应的测试用例名，即对应的函数名，添加测试类的实例化对象，即测试类中的具体函数名
#即父类中存在初始化参数methodName,
#在下述中对应的值为methodName=test_add_two_positive
# suit.addTest(TestAdd("test_add_two_positive"))
# suit.addTest(TestAdd("test_add_two_negative"))
# suit.addTest(TestAdd("test_sub_two_zero"))
# suit.addTest(TestAdd("test_sub_two_positive"))
# suit.addTest(TestAdd("test_sub_two_negative"))


#方法二
#实例化对象
loader = unittest.TestLoader()
#可加载某个测试类/模块中的所有测试用例
suit.addTest(loader.loadTestsFromTestCase(TestAdd)) #添加某个测试的类
suit.addTest(loader.loadTestsFromTestCase(TestSub))

#导入ddt的测试用例进入到suit中
suit.addTest(loader.loadTestsFromTestCase(Test_Add_ddt))
#通过模块名导入
# suit.addTest(loader.loadTestsFromModule(modulename))

# #依据用例的Test_Add类来确定传参的数目
# suit.addTest(Test_Add(a =2,b=3,expected=4,test_des="2+3",methodName="test_add_two_nums"))
# suit.addTest(Test_Add(1,2,3,"2+3","test_add_two_nums"))
#使用test_date数组来传数据
# for datas in test_data0:
#     suit.addTest(Test_Add(datas[0],datas[1],datas[2],datas[3],"test_add_two_nums"))
# for item in test_data1:
#     suit.addTest(Test_Add(item[2],item[3],item[4],item[1],"test_add_two_nums"))
for item in test_data2:
    suit.addTest(Test_Add(item["Param_a"],item["Param_b"],item["ExpectedResult"],item["title"],"test_add_two_nums",item["id"]+1))
# #依据用例的Test_Add类来确定传参的数目
# suit.addTest(Test_Add(a =2,b=3,expected=4))

#执行用例TextTestRunner
# with open("test_result.txt",'w+',encoding='utf-8') as res_file:
#     #TextTestRunner可将测试结果保存到文件中，verbosity修改显示的模式
#     runner = unittest.TextTestRunner(res_file,verbosity=2)
with open("test_result.html",'wb+') as res_file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(res_file, verbosity=2,title="Auto_test_0626",description="接口自动化学习1-0626",tester="Luht")
    runner.run(suit)

# if __name__ == '__main__':
#     unittest.main()