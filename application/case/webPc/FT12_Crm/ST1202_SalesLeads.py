
import win32api

import win32con
from selenium.webdriver.common.action_chains import ActionChains

from public.webClass import *


class SalesLeads(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        WebLogin.submit(self)
        driver = self.driver
        # 打开菜单
        WebMenu.full_text(self, "客户关系", "售前管理", "销售机会")
        # 移动到页面底部，防止对象遮挡
        WebForm.top(self, 0)
        driver.switch_to.frame("frame_tab_PM001072")

    """CRM-售前管理-销售机会-新增单据功能"""
    def test_1202_01_Add(self):
        """CRM-售前管理-销售机会-新增单据功能"""
        driver = self.driver
        # 进入到新增页面
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000316")
        v_tim = time.strftime("%Y-%m-%d %H:%M:%S")

        # 添加业务伙伴
        driver.find_element_by_xpath("//*[@id='CompositeField2_Container']/div/div/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        driver.find_element_by_id("txtSearchText").send_keys("C")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(2)
        driver.find_elements_by_class_name("x-grid3-row")[random.randint(0, 8)].click()
        driver.find_element_by_id("btnSelect").click()
        driver.switch_to.parent_frame()
        time.sleep(1)
        # 销售机会
        driver.find_element_by_id("Name").send_keys("销售机会" + v_tim)
        v_lines = driver.find_element_by_xpath("//*[@id='gpOPR1']")
        ActionChains(driver).context_click(v_lines).perform()
        driver.find_element_by_link_text("添加行").click()
        time.sleep(1)

        # ------阶段页签------
        # 阶段-开始日期
        v_date_start = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[2]"
        )
        ActionChains(driver).double_click(v_date_start).perform()
        driver.find_element_by_id("StartDate").click()
        time.sleep(1)
        # 操作键盘 Enter 键
        win32api.keybd_event(13, 0, 0, 0)
        # 操作键盘 Enter 键-释放按键
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(1)
        # 阶段-结算日期
        v_date_end = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[3]"
        )
        ActionChains(driver).double_click(v_date_end).perform()
        driver.find_element_by_id("dfCloseDate").click()
        time.sleep(1)
        win32api.keybd_event(13, 0, 0, 0)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        driver.find_element_by_id("gpOPR1").click()
        time.sleep(1)
        # 销售员
        v_date_saler = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[5]"
        )
        ActionChains(driver).double_click(v_date_saler).perform()
        time.sleep(1)
        v_saler = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div[4]/div/span"
        )
        ActionChains(driver).click(v_saler).perform()
        time.sleep(2)
        driver.switch_to.frame("winAdd_IFrame")
        v_line_saler = driver.find_elements_by_class_name("x-grid3-row")
        v_line_saler[1].click()
        driver.find_element_by_id("btnSelect").click()
        driver.switch_to.parent_frame()
        time.sleep(1)
        # 阶段
        v_add_end = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[6]"
        )
        ActionChains(driver).double_click(v_add_end).perform()
        time.sleep(1)
        v_phase = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div[5]/div/span"
        )
        ActionChains(driver).click(v_phase).perform()
        time.sleep(2)
        driver.switch_to.frame("winAdd_IFrame")
        v_type = driver.find_elements_by_class_name("x-grid3-row")
        v_type[random.randint(0, len(v_type)-1)].click()
        driver.find_element_by_id("Button1").click()
        time.sleep(1)
        driver.switch_to.parent_frame()
        # 潜在金额
        v_money = driver.find_element_by_xpath(
            "//*[@id='gpOPR1']/div/div/div/div/div[2]/div/div/table/tbody/tr/td[8]"
        )
        ActionChains(driver).double_click(v_money).perform()
        time.sleep(1)
        driver.switch_to.active_element.send_keys(random.randint(100, 9999))

        # ------常规页签------
        driver.find_element_by_link_text("常规").click()
        driver.find_element_by_xpath("//*[@id='ChnCrdCode_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_type = driver.find_elements_by_class_name("x-grid3-row")
        v_type[random.randint(0, len(v_type) - 1)].click()
        driver.find_element_by_id("btnSelect").click()
        driver.switch_to.parent_frame()
        time.sleep(1)
        # 常规页签-业务伙伴合作项目
        driver.find_element_by_xpath("//*[@id='PrjCode_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_type = driver.find_elements_by_class_name("x-grid3-row")
        v_type[random.randint(0, len(v_type) - 1)].click()
        driver.find_element_by_id("Button11").click()
        driver.switch_to.parent_frame()
        time.sleep(1)
        # 常规页签-行业
        driver.find_element_by_xpath("//*[@id='Industry_Container']/div/span").click()
        time.sleep(3)
        driver.switch_to.frame("winAdd_IFrame")
        v_type = driver.find_elements_by_class_name("x-grid3-row")
        v_type[random.randint(0, len(v_type) - 1)].click()
        driver.find_element_by_id("Button1").click()
        driver.switch_to.parent_frame()
        time.sleep(1)
        # 常规页签-备注
        driver.find_element_by_id("Memo").send_keys("Python 自动添加" + v_tim)

        driver.find_element_by_id("btnSave").click()
        time.sleep(3)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "成功" in i.text:
                print(i.text)
            else:
                print(i.text)
                driver.get_screenshot_as_file(propath() + "picture/erp/test_1202_01_Add.jpg")
                unittest.expectedFailure("test_1202_01_Add")

    """CRM-售前管理-销售机会-客户编号为空穿透提示"""
    def test_1202_02_Client(self):
        """CRM-售前管理-销售机会-客户编号为空穿透提示"""
        driver = self.driver
        # 进入到新增页面
        driver.find_element_by_id("btnAdd").click()
        time.sleep(3)
        driver.switch_to.default_content()
        driver.switch_to.frame("frame_tab_PM000316")

        # 客户主数据穿透
        driver.find_element_by_id("btnGoOCRD").click()
        time.sleep(2)
        v_tip = driver.find_elements_by_class_name("ext-mb-text")
        for i in v_tip:
            if "业务伙伴代码为空" in i.text:
                print(i.text)
            else:
                print(i.text)
                driver.get_screenshot_as_file(propath() + "picture/erp/test_1202_02_Client.jpg")
                unittest.expectedFailure("test_1202_02_Client")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    testsuit = unittest.TestSuite()
    testsuit.addTest(SalesLeads("test_1202_01_Add"))
    runner = unittest.TextTestRunner()
    runner.run(testsuit)