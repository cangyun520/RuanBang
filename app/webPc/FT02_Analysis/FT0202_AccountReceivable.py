# encoding:utf-8
from public.webClass import *
from public.sqlConnect.sqlServer import *
from public.config import *
import re


class ContractList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.submit(self)
        # 打开菜单
        WebMenu.full_text(self, "经营分析", "应收款情况")

    """经营分析-应收款情况"""
    def test_0202_01_Overdue(self):
        """应收款情况-逾期60天"""
        dr = self.driver
        _overdue = dr.find_element_by_id("paymentTotal").text
        _overdue = re.match('\d', _overdue)
        # 取数据库sum值
        with open(DATA_PATH + "/text/overdue60day.txt", 'rb') as file:
            _data = file.read()
        total = Sqlserverdb().queryOne(_data)
        total = total[0]
        total = int(round(total, 2))
        if int(_overdue[0]) == total:
            print("超过60天账龄款项数相同")
        else:
            dr.get_screenshot_as_file(REPORT_PATH + "webPc/test_0202_01_TotalMoneyCheck.png")
            unittest.expectedFailure("test_0202_01_TotalMoneyCheck")

        """应收款情况-本期应收未收金额"""
        _sumReceivable = dr.find_element_by_id("uncollectedTotal").text
        # 链式replace()
        _sumReceivable = _sumReceivable.replace(',', '').replace('元', '')
        _sumReceivable = get_trim(_sumReceivable)
        print(_sumReceivable)
        # 取数据库sum值
        with open(DATA_PATH + "/text/sumRexwivable.txt", 'rb') as file:
            _data = file.read()
        total = Sqlserverdb().queryOne(_data)
        total = total[0]
        total = float(round(total, 2))
        print(total)
        # 数值对比
        if float(_sumReceivable) <= total:
            print("超过60天本期应收未收金额--")
        else:
            dr.get_screenshot_as_file(REPORT_PATH + "webPc/test_0202_01_TotalMoneyCheck.png")
            unittest.expectedFailure("test_0202_01_TotalMoneyCheck")

    def test_0202_02_ding(self):
        pass
        dr = self.driver
        _dings = dr.find_elements_by_class_name("rb-row-button")
        for i in _dings:
            if i.text == "DING":
                i.click()
                timesl(2)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()