# encoding:utf-8
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error

from common.log import logger

from config.config import REPORT_PATH

"""
Created by Arvin.liu 15807146017
Date :2018-06-04.
"""
"""
邮件类。用来给指定用户发送邮件。可指定多个收件人，可带附件。
"""


class Email:
    def __init__(self, server, sender, password, receiver, title, message=None, path=None):
        """初始化Email
        param title: 邮件标题，必填。
        param message: 邮件正文，非必填。
        param path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
        param server: smtp服务器，必填。
        param sender: 发件人，必填。
        param password: 发件人密码，必填。
        param receiver: 收件人，多收件人用“；”隔开，必填。
        """
        self.title = title
        self.message = message
        self.files = path
        self.msg = MIMEMultipart('related')
        self.server = server
        self.sender = sender
        self.password = password
        self.receiver = receiver

    def _attach_file(self, att_file):
        """将单个文件添加到附件列表中"""
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)
        logger.info('attach file {}'.format(att_file))

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        # 邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))

        # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)  # 连接sever
        except (gaierror and error) as e:
            logger.exception('发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. {1}'.format(e))
        else:
            try:
                smtp_server.login(self.sender, self.password)  # 登录
            except smtplib.SMTPAuthenticationError as e:
                logger.exception('用户名密码验证失败！{1}'.format(e))
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())  # 发送邮件
                logger.info('发送邮件"{0}"成功! 收件人：{1}。'.format(self.title, self.receiver))
                print('发送邮件"{0}"成功! 收件人：{1}。'.format(self.title, self.receiver))
            finally:
                smtp_server.quit()  # 断开连接


if __name__ == "__main__":
    # report = REPORT_PATH + '\\FTReport\\20180720FT_webPC.htm'
    report = REPORT_PATH + '\\FTReport\\20180727FT_webPC.htm'
    mail_smtp = "smtp.126.com"              # SMTP服务器
    sender = "qinliulangzhou@126.com"       # 用户名
    password = "qin130sqm"                       # 授权密码，非登录密码
    # password = cdbxikdixeppcadg                 # QQ
    receivers = '405367236@qq.com;whonline08@126.com'           # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    content = '我用Python+Selenium进行自动化测试'
    title = '自动化测试报告'                            # 邮件主题

    e = Email(title=title,
              message=content,
              receiver=receivers,
              server=mail_smtp,
              sender=sender,
              password=password,
              path=report
              )
    e.send()
