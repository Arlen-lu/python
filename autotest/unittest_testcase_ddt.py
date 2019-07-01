import unittest
from ddt import ddt,data
from read_config import ReadConfig
import HTMLTestRunnerNew
#导入测试报告模块
import HTMLTestRunnerNew
#导入被测试类(即需要测试的接口代码)
from unittest_math_method import MathMethod
from unittest_testcase_excel import DoExcel
from unittest_testcase_excel import GetExcel
excel_path = GetExcel("testdata.xlsx").Get_Excel_Path()
excel_title = "testdata"
button = ReadConfig().read_config("case.config",'FLAG','button')
case_id_list = eval(ReadConfig().read_config("case.config",'FLAG','cse_id_list'))
test_data = DoExcel(excel_path,excel_title).do_excel2(button,case_id_list) #列表数据
#优化测试用例
@ddt
class Test_Add_ddt(unittest.TestCase): #测试类

    def setUp(self):
        self.t = MathMethod()
        # self.doexcel = DoExcel()
        print("********************")
        print("Test Begin:")
        # print("Test describtion:{0}".format(self.test_des))

    def tearDown(self):
        print("Test finished!!")
        print("********************")

    @data(*test_data)
    def test_add_two_nums(self,item):
        # print("测试数据{0}".format(item))
        excel_path = GetExcel("testdata.xlsx").Get_Excel_Path()
        excel_title = "testdata"
        res = self.t.add(item['Param_a'],item['Param_b']) #需要初始化num_a,num_b,expected
        print("Test describtion:{0}".format(item['title']))
        print("Param_a:{0}".format(item['Param_a']))
        print("Param_b:{0}".format(item['Param_b']))
        try:
            self.assertEqual(item['ExpectedResult'],res)
            test_result = 'Pass'
        except AssertionError as e:
            test_result = 'Fail'
            print("wrong msg:{0}".format(e))
            raise e
        finally:
            print("finally")
            print("TestResult:{0}".format(test_result))
            DoExcel(excel_path,excel_title).Write_Back(row=item['id']+1,ActualResult=res,TestResult=test_result)

suit = unittest.TestSuite()
loader = unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(Test_Add_ddt))

#执行用例TextTestRunner
# with open("test_result.txt",'w+',encoding='utf-8') as res_file:
#     #TextTestRunner可将测试结果保存到文件中，verbosity修改显示的模式
#     runner = unittest.TextTestRunner(res_file,verbosity=2)
# with open("test_result.html",'wb+') as res_file:
#     runner = HTMLTestRunnerNew.HTMLTestRunner(res_file, verbosity=2,title="Auto_test_0628",description="接口自动化学习1-0628",tester="Luht2")
#     runner.run(suit)
if __name__ =="__main__":
    unittest.main()