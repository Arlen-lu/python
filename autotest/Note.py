#更新pip
#python -m pip install --upgrade pip
#写用例：TestCase  		
#加载用例：TestSuit+TestLoader
#比对结果：Assert
#执行并处结果：TextTestRunner
#报告：HtmlTestReport

# 1.被测试函数
# 2.调用unittest.TestCase父类，进行测试用例的编写->新建测试类，编写函数，内包含具体的测试用例，setUp，tearDown测试环境搭建+Assert 测试结果比对，判定
	# 2.1 try:
            # self.assertEqual(0,res)#断言函数调用
        # except AssertionError as e:
            # print("测试错误，错误信息为{0}".format(e))
			# raise e#抛出错误信息
# 3.unittest.TestSuit父类，将测试用例放到一个组合中去--->unittest.TestSuit.addTest方法，加入测试用例到suit中
	# 3.1 suit.addTest([测试类名]([函数名]))---->以单测试用例导入
	# 3.2 unittest.TestLoader().loadTestsFromTestCase/loadTestsFromModule--->以测试类/模块导入，不需要具体到具体的测试用例
# 4.unittest.TextTestRunner.run执行用例，并输出测试报告
	# 4.1 使用 HTMLTestRunnerNew.HTMLTestRunner.run  测试报告更加详细
	
#openpyxl
#ddt

#文件的位置，需要注意
#data: contains as many arguments as values you want to feed to the test.
# file_data: will load test data from a JSON or YAML file.
#@unittest.skip()可以用来装饰类的方法，也可以用来装饰class，将这个class全部跳过.
# @unittest.skip(reason)
# 直接跳过这条测试用例，需要给出跳过的理由

# @unittest.skipIf(condition, reason)
# 跳过这条用例，如果condition值为True

# @unittest.skipUnless(condition, reason)

# @unittest.expectedFailure

# exception unittest.SkipTest(reason)

# %(levelno)s: 打印日志级别的数值
# %(levelname)s: 打印日志级别名称
# %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s: 打印当前执行程序名
# %(funcName)s: 打印日志的当前函数
# %(lineno)d: 打印日志的当前行号
# %(asctime)s: 打印日志的时间
# %(thread)d: 打印线程ID
# %(threadName)s: 打印线程名称
# %(process)d: 打印进程ID
# %(message)s: 打印日志信息


#接口测试知识点
#cookie:在客户端存储用户的数据
#session 在服务器端记录用户的请求状态，一般默认时间为30mins
# session_id 会存在cookie中，每次请求cookie中的所有信息都会传送给服务器，
# 服务器通过session_id来识别是否是同一个用户的请求。不是同一个用户的话，就会要求用户重新登陆。
# 上述机制的产生，是由于Http请求是无状态的
#授权和鉴权
# 鉴权：访问的接口是否正常，是否是非法访问，绕过前端访问，token
# 授权：是否具有访问接口的权限，是唯一的，全局的，动态的，具备一定特性
# 10-8上课课外补充知识链接
# https://jingyan.baidu.com/article/375c8e19770f0e25f2a22900.html  ok
# https://www.cnblogs.com/nickjiang/p/9148136.html cookie 和session的区别&token ok
#cookie:cookie是一门客户端技术，一般是由服务器生成返回给浏览器客户端来保存的，
# 并且cookie是以键值对的形式保存在浏览器客户端的，每一个cookie都会有名称，值，过期时间...。
# 应用:1.登录记住用户名,2.记录用户浏览记录

#session:session是服务端的会话技术，
# 当用户登录了系统，服务器端的web容器就会创建一个会话，
# 此会话中可以保存登录用户的信息，并且也是以键值对的形式去保存的，
# 现在大部分系统都是使用的session技术来做的鉴权（权限鉴定），即：当用户登录完了才可以访问系统中的一些页面和数据。

#token机制 多用于app中

# https://blog.csdn.net/sjy8207380/article/details/79232644  ok 不太懂
# http://docs.python-requests.org/zh_CN/latest/   着重看，requests介绍
# http://docs.python-requests.org/zh_CN/latest/user/quickstart.html 同上

# Get,Post区别
#Get:提交的参数会拼接到URL里面去，安全性低，传递的数据量比较小
#Post:参数不会拼接到URL里面去，post用额外的数据格式去传递，如json，xml，传递的数据量比较大

#Jmeter
#域名+路径 = 接口地址
#课堂派：
#域名：www.ketangpai.com
#地址:/UserApi/login

#抓包
#若你的请求必须是在登陆的情况下完成，需要加cookie
#授权key，key授权码通过参数导入

#git
