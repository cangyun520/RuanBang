# -*- coding: utf-8 -*-
from public.log import logger
from public.webClass import *

from config import REPORT_PATH

'''
思路：
1.先定位到报表目录
2.找到最新报表
3.用谷歌浏览器打开本地html文件
4.定位到错误用例，并输出到指定text
5.重新执行错误用例
'''


class RunResult(unittest.TestCase):
    """登录后首页"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        dr = self.driver
        v_tim = time.strftime("%Y%m%d")
        _file = REPORT_PATH + '/FTReport/' + v_tim + 'FT_webPC.htm'
        dr.maximize_window()
        dr.get(_file)
        time.sleep(3)

    def test_list(self):
        driver = self.driver
        _errors = driver.find_elements_by_class_name("errorCase")
        _passs = driver.find_elements_by_class_name("testcase")
        for i in _errors:
            # str = i.text
            # result = str.split(':')[0]      # 后面参数0表示向左，1表示向右
            print(i.text)
        # format 格式化输出 数字
        logger.info("总计运行用例 {0} 条，失败：{1} 条".format((len(_errors)+len(_passs)), len(_errors)))
        print("总计集成测试运行用例 {0} 条，失败：{1} 条".format((len(_errors)+len(_passs)), len(_errors)))

    def tearDown(self):
        self.driver.quit()
