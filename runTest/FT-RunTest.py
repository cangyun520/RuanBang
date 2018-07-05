
from HTMLTestRunner import HTMLTestRunner
from public.webClass import *

'''
    *   SASS功能集成测试报告
    *   指定测试用例为当前文件夹下的test_case目录
    *   通过自定函数获取当前文件所在路径
    *   获取最新测试报告，并打印运行错误用例
    *   把结果发送到指定邮箱
    *   Arvin
    *   2017-06-13
'''
v_tim = time.strftime("%Y%m%d")
test_dir = propath() + "/application/webPc"
# discover会根据测试目录 匹配查找测试用例文件，并将查找到的测试用例组装到测试套件中
discover = unittest.defaultTestLoader.discover(
    test_dir,
    pattern='FT*.py'
)
# 报告文件存放路径
FileName = propath() + 'report/FTRport/' + v_tim + 'FT_online.htm'
fp = open(FileName, 'wb')
runner = HTMLTestRunner(
    stream=fp,
    title='online功能集成自动化测试',
    description='online自动化测试——主流程功能测试执行结果统计'
)
runner.run(discover)
fp.close()


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
        # print(('最新的文件为：'+v_list[-1]))
        # 最新文件的绝对路径
        v_url = os.path.join(resault_dir, v_list[-1])
        driver.maximize_window()
        driver.get(v_url)
        time.sleep(3)

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