# encoding:utf-8
from public.webClass import *
from public.sqlConnect.sqlServer import *
from public.log import logger
from public.mail import *


class ContractList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.submit(self)
        # 打开菜单
        WebMenu.full_text(self, "合同管理", "签约明细")

    """合同-合同列表"""
    def test_0602_01_TotalMoneyCheck(self):
        """合同-合同列表"""
        dr = self.driver
        _tds = dr.find_elements_by_css_selector(".rb-gridview-sum-roll>table>tbody>tr>td")
        for i in _tds:
            if i.get_attribute("data-id") == "money":
                # 文本转译
                money = (i.text).replace(',', '')
                break

        # 取数据库sum值
        _sql = "SELECT SUM(money) FROM wht_Contract WHERE deleted = 0"
        total = Sqlserverdb().queryOne(_sql)
        total = total[0]
        total = str(round(total, 2))

        if money == total:
            logger.info("列表金额{0}，数据查询金额{1}".format(money, total))
        else:
            dr.get_screenshot_as_file(PICTURE_PATH + "/webPc/test_0602_01_TotalMoneyCheck.png")
            unittest.expectedFailure("test_0602_01_TotalMoneyCheck")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

