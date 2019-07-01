#日志:记录系统的操作 记录代码的运行
#即log
#日志级别：debug、# info、warning、error、critical
#logging python日志系统模块，默认存在
#收集日志：收集器(root)
#默认只收集warning及以上级别的信息
#输出日志：输出控制台

import logging

class MyLog():

#升级点：1.name，level，formatter，filehandler可用变量代替，将相关信息存储到config文件中去
    def my_log(self,level,msg):
        #自定义日志收集器
        #并设置收集器名称为”Arlen“
        my_logger = logging.getLogger("Arlen")
        my_logger.setLevel("DEBUG") #控制收集的级别，以上级别
        #自定义输出控制台，来设置能输出所有的警告信息

        #设置日志输出的格式
        formatter= logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s: %(message)s')
        ch = logging.StreamHandler() #输出到控制台，创建实例
        ch.setLevel("DEBUG")#控制输出的级别，以上级别,过滤作用
        #输出控制台应用输出的格式
        ch.setFormatter(formatter)


        #将log输出到文件中
        fh = logging.FileHandler("log_learn.txt")#
        fh.setLevel("DEBUG")#控制输出的级别，以上级别，过滤作用
        fh.setFormatter(formatter)

        #将自定义的收集器与输出控制台对接起来
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        #输出
        if level =='DEBUG': #区分大小写
            my_logger.debug(msg)
        elif level =='INFO':
            my_logger.info(msg)
        elif level =='WARNING':
            my_logger.warning(msg)
        elif level =='ERROR':
            my_logger.error(msg)
        elif level =='CRITICAL':
            my_logger.critical(msg)

        #日志收集完成，移除渠道，否则日志输出会重复
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    #类中函数调用
    def debug(self,msg):
        self.my_log('DEBUG',msg)
    def info(self,msg):
        self.my_log('INFO',msg)
    def warning(self,msg):
        self.my_log('WARNING',msg)
    def error(self,msg):
        self.my_log('ERROR',msg)
    def critical(self,msg):
        self.my_log('CRITICAL',msg)

if __name__ =='__main__':
    #使用logging默认的收集器，则输出控制台为root
    logging.debug("debug")  #未输出
    logging.info("info") #未输出
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")
    logging.critical("**************************")

    my_logger = MyLog() #区分大小写
    my_logger.debug('debug')
    my_logger.info("info")
    my_logger.warning("warning")
    my_logger.error("error")
    my_logger.critical("critical")