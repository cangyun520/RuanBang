# encoding:utf-8
from public.webClass import *
from public.sqlConnect.sqlServer import *
from public.log import logger
from public.HTMLTestRunner_PY3 import HTMLTestRunner


class ContractList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.submit(self)
        # 打开菜单
        WebMenu.full_text(self, "合同管理", "合同")

    """合同-合同列表"""
    def test_0602_01_TotalMoneyCheck(self):
        """合同-新增合同"""
        dr = self.driver
        _tds = dr.find_elements_by_css_selector(".rb-gridview-sum-roll>table>tbody>tr>td")
        for i in _tds:
            if i.get_attribute("data-id") == "money":
                money = (i.text).replace(',', '')
                break

        # 取数据库sum值
        _sql = "SELECT SUM(money) FROM wht_Contract WHERE deleted = 0"
        total = Sqlserverdb().queryOne(_sql)
        total = total[0]
        total = str(round(total, 2))

        if money == total:
            logger.info("合同列表金额相同")
        else:
            dr.get_screenshot_as_file(propath() + "picture/webPc/test_0602_01_TotalMoneyCheck.png")
            unittest.expectedFailure("test_0602_01_TotalMoneyCheck")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
        runner.run(ContractList('test_0602_01_TotalMoneyCheck'))
