# -*- coding: utf-8 -*-
from utils.webClass import *

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
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        driver = self.driver
        # 定义文件目录
        resault_dir = propath() + 'report/FTRport/'
        # 遍历目录
        v_list = os.listdir(resault_dir)
        # 重新按时间对目录文件进行排序
        v_list.sort(
            key=lambda fn: os.path.getatime(resault_dir+'/'+fn)
        )
        print(('最新的文件为：'+v_list[-1]))
        # 最新文件的绝对路径
        v_url = os.path.join(resault_dir, v_list[-1])
        driver.maximize_window()
        driver.get(v_url)
        time.sleep(3)

    def test_list(self):
        driver = self.driver
        v_list = driver.find_elements_by_class_name("errorCase")
        for i in v_list:
            str = i.text
            # result = str.split(':')[0]      # 后面参数0表示向左，1表示向右
            # print(str)
        # %d 格式化输出 数字
        print("运行失败总计：%d" % (len(v_list)))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
