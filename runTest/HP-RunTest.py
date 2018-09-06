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
test_dir = APP_PATH + "/homePage"
# discover会根据测试目录 匹配查找测试用例文件，并将查找到的测试用例组装到测试套件中
discover = unittest.defaultTestLoader.discover(
    test_dir,
    pattern='FT*.py'
)
# 报告文件存放路径
FileName = REPORT_PATH + '\\HPReport\\' + v_tim + 'FT_webPC.htm'

fp = open(FileName, 'wb')
runner = HTMLTestRunner(
    stream=fp,
    title='主页定义系统集成自动化测试',
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


if __name__ == "__main__":
    mail_smtp = "smtp.qq.com"                    # SMTP服务器
    sender = "405367236@qq.com"                 # 用户名
    password = 'cdbxikdixeppcadg'               # QQ授权密码，非登录密码
    # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    receivers = 'whonline08@126.com;' \
                'bill.wang@softnation.cn;' \
                'sengmitnick@163.com;' \
                'dingj@yuandingyun.net;' \
                'w.huang@softnation.cn;' \
                'fortunearterial@dingtalk.com'

    content = '今天的自动化测试运行结果，请查收'
    title = '自动化测试报告'                       # 邮件标题
    e = Email(title=title,
              message=content,
              receiver=receivers,
              server=mail_smtp,
              sender=sender,
              password=password,
              path=FileName
              )
    e.send()
