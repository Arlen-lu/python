import unittest
#导入测试报告模块
import HTMLTestRunnerNew
#导入被测试类(即需要测试的接口代码)
from unittest_math_method import MathMethod
from unittest_testcase_excel import DoExcel
from unittest_testcase_excel import GetExcel
class TestAdd(unittest.TestCase):

    #执行用例前，测试环境的搭建
    def setUp(self):
        print("测试开始:")
        #实例化对象被测试类
        self.t = MathMethod()
    #执行完成后，测试环境的初始化
    def tearDown(self):
        print("测试完成！！")

    #写用例，每一条用例都是一个函数
    #测试两个0相加
    def test_add_two_zero(self):
        # t = MathMethod()
        res = self.t.add(0,0)
        #异常处理
        try:
            self.assertEqual(0,res)#断言函数调用
        except AssertionError as e:
            print("测试错误，错误信息为{0}".format(e))
            raise e#抛出错误信息
        # self.assertEqual(0,res)#self直接调用，说明该函数来自父类
        # print("Result1:{0}".format(res))

    #两个正数相加
    def test_add_two_positive(self):
        # t = MathMethod()
        res = self.t.add(1,4)
        #异常处理
        try:
            self.assertEqual(0,res)#断言函数调用
        except AssertionError as e:
            print("测试错误，错误信息为{0}".format(e))
            raise e#抛出错误信息
        # print("Result1:{0}".format(res))

    #两个负数相加
    def test_add_two_negative(self):
        # t = MathMethod()
        res = self.t.add(-1,-4)
        #异常处理
        try:
            self.assertEqual(0,res)#断言函数调用
        except AssertionError as e:
            print("测试错误，错误信息为{0}".format(e))
            raise e#抛出错误信息
        # self.assertEqual(0,res)
        # print("Result1:{0}".format(res))

class TestSub(unittest.TestCase):

    #执行用例前，测试环境的搭建
    def setUp(self):
        print("测试开始:")
        #实例化对象被测试类
        self.t = MathMethod()
    #执行完成后，测试环境的初始化
    def tearDown(self):
        print("测试完成！！")

    #测试两个0相减
    def test_sub_two_zero(self):
        # t = MathMethod()
        res = self.t.sub(0,0)
        #异常处理
        try:
            self.assertEqual(0,res)#断言函数调用
        except AssertionError as e:
            print("测试错误，错误信息为{0}".format(e))
            raise e#抛出错误信息
        # self.assertEqual(0,res) #期望值，实际值
        # print("Result1:{0}".format(res))

    #两个正数相减
    def test_sub_two_positive(self):
        # t = MathMethod()
        res = self.t.sub(1,4)
        #异常处理
        try:
            self.assertEqual(0,res)#断言函数调用
        except AssertionError as e:
            print("测试错误，错误信息为{0}".format(e))
            raise e#抛出错误信息
        # self.assertEqual(0,res)
        # print("Result1:{0}".format(res))

    #两个负数相减
    def test_sub_two_negative(self):
        # t = MathMethod()
        res = self.t.sub(-1,-4)
        #异常处理
        try:
            self.assertEqual(0,res)#断言函数调用
        except AssertionError as e:
            print("测试错误，错误信息为{0}".format(e))
            raise e#抛出错误信息
        # self.assertEqual(0,res)
        # print("Result1:{0}".format(res))

#优化测试用例
class Test_Add(unittest.TestCase): #测试类

    def __init__(self,a,b,expected,test_des,methodName,row):
        #由于父类存在初始化函数。故当前子函数不能全部覆盖重写，需要超继承，即保存父类，新增子类初始化数据
        super(Test_Add,self).__init__(methodName)#保留父类的初始化参数,该参数必须传，可传变量，也可传实际值
    # def __init__(self,a,b,expected):
    #     super(Test_Add,self).__init__("test_add_two_nums")#传实际值，即对应的函数名
        self.num_a = a
        self.num_b = b
        self.expected = expected
        self.test_des = test_des#测试用例说明
        self.row = row


    def setUp(self):
        self.t = MathMethod()
        # self.doexcel = DoExcel()
        print("Test Begin:")
        print("Test describtion:{0}".format(self.test_des))

    def tearDown(self):
        print("Test finished!!")

    def test_add_two_nums(self):
        excel_path = GetExcel("testdata.xlsx").Get_Excel_Path()
        excel_title = "testdata"
        res = self.t.add(self.num_a,self.num_b) #需要初始化num_a,num_b,expected
        print("Param_a:{0}".format(self.num_a))
        print("Param_b:{0}".format(self.num_b))
        try:
            self.assertEqual(self.expected,res)
            test_result = 'Pass'
        except AssertionError as e:
            test_result = 'Fail'
            print("Test Fail，wrong msg:{0}".format(e))
            raise e
        finally:
            print("finally")
            DoExcel(excel_path,excel_title).Write_Back(row=self.row,ActualResult=res,TestResult=test_result)

if __name__ =="__main__":
    unittest.main()