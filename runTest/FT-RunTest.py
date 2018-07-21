# encoding:utf-8
from public.HTMLTestRunner_PY3 import HTMLTestRunner
from public.webClass import *
from public.config import APP_PATH, REPORT_PATH
from public.mail import *

'''
    *   Arvin.liu
    *   2018-06-13
'''
v_tim = time.strftime("%Y%m%d")
test_dir = APP_PATH + "/webPc"
# discover会根据测试目录 匹配查找测试用例文件，并将查找到的测试用例组装到测试套件中
discover = unittest.defaultTestLoader.discover(
    test_dir,
    pattern='FT*.py'
)
# 报告文件存放路径
FileName = REPORT_PATH + '/FTRport/' + v_tim + 'FT_webPC.htm'
fp = open(FileName, 'wb')
runner = HTMLTestRunner(
    stream=fp,
    title='王伟合同系统集成自动化测试',
    description='webPC自动化测试——主流程功能测试执行结果统计<br/>\
                *   SASS功能集成测试报告<br>\
                *   指定测试用例为当前文件夹下的test_case目录<br>\
                *   通过自定函数获取当前文件所在路径<br>\
                *   获取最新测试报告，并打印运行错误用例<br>\
                *   把结果发送到指定邮箱<br>\
                '
)
runner.run(discover)
fp.close()


class RunResult(unittest.TestCase):
    """登录后首页"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        dr = self.driver
        dr.maximize_window()
        dr.get(FileName)
        time.sleep(1)

    def test_list(self):
        driver = self.driver
        v_list = driver.find_elements_by_class_name("errorCase")
        if len(v_list) == 0:
            print("本次运行全部正确！！！")
        else:
            for i in v_list:
                # str = i.text
                # result = str.split(':')[0]      # 后面参数0表示向左，1表示向右
                print(i.text)
            # %d 格式化输出 数字
            print("运行失败总计：%d" % (len(v_list)))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    server = "smtp.126.com"  # SMTP服务器
    sender = "qinliulangzhou@126.com"  # 用户名
    password = "qin130sq"  # 授权密码，非登录密码
    sender = 'qinliulangzhou@126.com'  # 发件人邮箱(最好写全, 不然会失败)
    # receivers = '405367236@qq.com;506505739@qq.com;sengmitnick@163.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    receivers = '405367236@qq.com'
    message = '这是今天的测试报告，请查收！具体请看附件。'
    title = '王伟合同自动化测试报告'  # 邮件主题

    e = Email(title=title,
              message=message,
              receiver=receivers,
              server=server,
              sender=sender,
              password=password,
              path=FileName
              )
    e.send()
