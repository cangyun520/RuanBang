# encoding:utf-8
from public.webClass import *
from public.sqlConnect.sqlServer import *


class ContractList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.submit(self)
        # 打开菜单
        WebMenu.full_text(self, "合同管理", "合同")

    """合同-新增合同"""
    def test_0602_01_TotalMoneyCheck(self):
        """合同-新增合同"""
        dr = self.driver
        _tds = dr.find_elements_by_css_selector(".rb-gridview-sum-roll>table>tbody>tr>td")
        for i in _tds:
            if i.get_attribute("data-id") == "money":
                money = (i.text).replace(',', '')
                print(money)
                break

        # 取数据库sum值
        sql = "SELECT ROUND(SUM(money),2) FROM wht_Contract WHERE deleted = 0"
        total = Sqlserverdb().queryOne(sql)
        total = total[0]
        total = str(round(total, 2))
        print(total)

        if money == total:
            print("金额相同")
        else:
            dr.get_screenshot_as_file(propath() + "picture/webPc/test_0602_01_TotalMoneyCheck.png")
            unittest.expectedFailure("test_0602_01_TotalMoneyCheck")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()