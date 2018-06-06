
from utils.webClass import *


class Index(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        WebLogin.submit(self)

    def test_0101_Task(self):
        """onlin首页-查看我的任务-【收信】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"查看我的任务").click()
        time.sleep(3)
        driver.switch_to_frame("frame_tab_PM000789")
        v_Calendar = driver.find_element_by_id("ext-gen75")
        try:
            v_Calendar.is_displayed()
            print("我的任务页面-日历视图-显示正常")
        except ImportError:
            print("BUG 【日历视图】不显示")
        v_Calendar.click()
        time.sleep(3)
        v_List =driver.find_element_by_id("ext-gen19")
        try:
            v_List.is_displayed()
            print("我的任务页面-列表视图-显示正常")
        except ImportError:
            print("BUG 【列表视图】不显示，请检查日历界面")
            unittest.expectedFailure("test_0101_Task")
        time.sleep(3)

    # ------首页-个人信息------
    def test_0102_Work(self):
        """onlin首页-查看汇报给我的工作-【我收到的】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"查看汇报给我的工作").click()
        time.sleep(3)
        driver.switch_to_frame("frame_tab_PM000483")
        v_received = driver.find_element_by_link_text("我收到的")
        try:
            v_received.is_displayed()
            print("日志填报页面-显示正常")
        except ImportError:
            print("BUG ‘我收到的’不显示，请检查’我收到的‘界面是否正常")
            unittest.expectedFailure("test_0102_Work")
        v_received.click()

    def test_0103_Report(self):
        """onlin首页-查看我收藏的报表-【展开所有】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"查看我收藏的报表").click()
        time.sleep(3)
        driver.switch_to_frame("frame_tab_PM000014")
        v_Expand = driver.find_element_by_id("ext-gen54")
        try:
            v_Expand.is_displayed()
            print("我的收藏报表页面-显示正常")
        except ImportError:
            print("BUG ‘展开所有’不显示，请检查界面是否正常")
            unittest.expectedFailure("test_0106_Index")

    def test_0104_File(self):
        """onlin首页-查看我的文件-【上传】检查"""
        driver = self.driver
        driver.find_element_by_link_text(u"查看我的文件").click()
        time.sleep(3)
        driver.switch_to_frame("frame_tab_PM000815")
        v_Upload = driver.find_element_by_id("ext-gen40")
        try:
            v_Upload.is_displayed()
            print("个人文件柜页面-显示正常")
        except ImportError:
            print("BUG 【上传】不显示，请检查界面是否正常")
            unittest.expectedFailure("test_0103_Report")

    def test_0105_user(self):
        """onlin首页-个人信息-UI检查"""
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='ngSection']/div[1]/div/div[2]/div/ul/li[8]").click()
        time.sleep(3)
        driver.switch_to_frame("frame_tab_PM000988")
        var_update = driver.find_element_by_link_text(u"更新")
        try:
            var_update.is_displayed()
            print("个人信息-显示正常")
        except ImportError:
            print("BUG 个人信息-显示错误")
            unittest.expectedFailure("test_0105_user")
    # ------onlinebox首页模块------

    def test_0106_Index(self):
        driver = self.driver
        driver.find_element_by_css_selector("span.title").click()
        driver.find_element_by_link_text(u"管理驾驶舱").click()
        time.sleep(3)
        driver.switch_to_frame("frame_tab_PM001048")
        v_analysis = driver.find_element_by_xpath("html/body/div[1]/div[3]/div/div/div[1]/div/span[1]")
        try:
            v_analysis.is_displayed()
        except ImportError:
            print("BUG 管理驾驶舱页面显示异常")
        else:
            print("管理驾驶舱页面-销售分析区域加载正常")
        driver.switch_to_default_content()
        driver.find_element_by_link_text(u"HR首页").click()
        time.sleep(3)
        driver.switch_to_frame("frame_tab_PM001007")
        Index_a = ".//*[@id='form1']/div[3]/div/div/div[1]/div[2]/div/div[1]/div[1]/span[1]"
        v_personnel =driver.find_element_by_xpath(Index_a)
        try:
            v_personnel.is_displayed()
            print("HR报表页面-人员异动区域加载正常")
        except ImportError:
            print("BUG HR报表页面显示异常")
            unittest.expectedFailure("test_0106_Index")

    def test_0107_Approval(self):
        """onlin首页-查看所有流程审批"""
        driver = self.driver
        driver.find_element_by_link_text(u"查看所有审批流程").click()
        time.sleep(3)
        driver.switch_to_frame("frame_tab_PM000040")        # 切换到代办工作页面
        v_searchWK = driver.find_element_by_id("BtnSearchWK")
        try:
            v_searchWK.is_displayed()
            print("代办工作页面-显示OK")
        except ImportError:
            print("BUG 代办工作页面-显示异常")
            unittest.expectedFailure("test_0107_Approval")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(Index("test_001_Task"))
    testsuit.addTest(Index("test_002_Work"))
    # 获取当前时间
    v_tim = time.strftime("%y%m%d%H%M")
    # 定义报告存放路径
    FileName = 'F:/Autowebdriver/report/STRport/' + v_tim + ' ST01_Index.html'
    ReportFile = open(FileName,'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=ReportFile,
                            title="首页冒烟测试",
                            description="用例执行情况")
    # 运行测试用例集合
    runner.run(testsuit)
    ReportFile.close()
