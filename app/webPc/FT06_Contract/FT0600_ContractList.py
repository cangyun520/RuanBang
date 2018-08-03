# encoding:utf-8
from public.webClass import *
from public.log import logger
from public.downFile import *
import xlrd
from public.excelRead import *


# 更改Chrom默认下载路径
op = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_settings.popups': 0,   # 不弹窗
    'download.default_directory': DOWN_PATH     # 下载路径
}
op.add_experimental_option('prefs', prefs)

# 菜单目录
_menu = "签约明细"


class ContractList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=op)
        # 登录
        WebLogin.submit(self)
        # 打开菜单
        WebMenu.full_text(self, "合同管理", _menu)

    """合同-导出"""
    def test_0602_02_export(self):
        """合同-导出"""
        dr = self.driver
        _time = time.strftime("%Y-%m-%d")
        _tds = dr.find_elements_by_css_selector(".rb-gridview-sum-roll>table>tbody>tr>td")
        for i in _tds:
            if i.get_attribute("data-id") == "money":
                # 文本转译
                money = i.text
                break

        SAASPc.buttons(self, "导出")
        timesl(2)
        try:
            file_find("xlsx")
        except FileExistsError as e:
            dr.get_screenshot_as_file(PICTURE_PATH + "/webPc/test_0602_02_export.png")
            unittest.expectedFailure("test_0602_02_export")

        f = _menu + "(" + _time + ")" + ".xlsx"
        print(f)
        p = file_path(f)
        data = open_excel(p)
        table = data.sheets()[0]
        try:
            nrows = table.nrows
            print(nrows-2)
        except Exception as e:
            dr.get_screenshot_as_file(PICTURE_PATH + "/webPc/test_0602_01_TotalMoneyCheck.png")
            unittest.expectedFailure("test_0602_01_TotalMoneyCheck")
        timesl(1)
        file_remove(f)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

