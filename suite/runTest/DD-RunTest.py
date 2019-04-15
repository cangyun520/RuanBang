# encoding:utf-8
from public.HTMLTestRunner_PY3 import HTMLTestRunner
from public.mail import *
from public.webClass import *

from config import APP_PATH, REPORT_PATH

'''
    *   Arvin.liu
    *   2018-07-31
'''
v_tim = time.strftime("%Y%m%d")
test_dir = APP_PATH + "/dingtalk"
# discover会根据测试目录 匹配查找测试用例文件，并将查找到的测试用例组装到测试套件中
discover = unittest.defaultTestLoader.discover(
    test_dir,
    pattern='FT*.py'
)
# 报告文件存放路径
FileName = REPORT_PATH + '/DDReport/' + v_tim + 'Dingtalk.htm'
fp = open(FileName, 'wb')
runner = HTMLTestRunner(
    stream=fp,
    title='钉钉自定义主页系统集成自动化测试',
    description='钉钉移动端自动化测试——主流程功能测试执行结果统计<br/>\
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
    # SMTP服务器
    server = "smtp.126.com"
    # 用户名
    sender = "qinliulangzhou@126.com"
    # 授权密码，非登录密码
    password = "qin130sqm"
    # 发件人邮箱(最好写全, 不然会失败)
    sender = 'qinliulangzhou@126.com'
    # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    receivers = '405367236@qq.com;' \
                'bill.wang@softnation.cn;' \
                'sengmitnick@163.com;' \
                'dingj@yuandingyun.net;' \
                'w.huang@softnation.cn;' \
                'fortunearterial@dingtalk.com;' \
                'zhoumeng9998@dingtalk.com'
    # receivers = '405367236@qq.com'
    message = '这是钉钉今天的测试报告，请查收！具体请看附件。'
    # 邮件主题
    title = '钉钉自定义主页自动化测试报告' + v_tim

    e = Email(title=title,
              message=message,
              receiver=receivers,
              server=server,
              sender=sender,
              password=password,
              path=FileName
              )
    e.send()
