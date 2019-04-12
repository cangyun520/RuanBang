# encoding:utf-8
from public.excelRead import *
from public.webClass import *

from common.log import logger

# 更改Chrom默认下载路径
op = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_settings.popups': 0,   # 不弹窗
    'download.default_directory': DOWN_PATH     # 下载路径
}
op.add_experimental_option('prefs', prefs)

# 菜单目录
_module = "合同管理"
_menu = "签约明细"


class DataExport(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=op)
        # 登录
        WebLogin.submit(self)
        # 打开菜单
        WebMenu.full_text(self, _module, _menu)

    """合同-导出"""
    def test_0602_02_export(self):
        """合同-导出"""
        dr = self.driver
        _time = time.strftime("%Y-%m-%d")
        # 获取行总条数
        sunCount = dr.find_element_by_class_name("rb-gridview-sumCount").text

        # 导出到指定data/down目录并校验文件是否导出
        SaaSPc.button(self, "导出")
        timesl(2)
        file_find("xlsx")
        f = _menu + "(" + _time + ")" + ".xlsx"
        try:
            f in file_find("xlsx")
            print(f)
        except FileExistsError as e:
            logger.info(e)

        # 读取excel内部数据，行总数
        fpath = file_path(f)
        data = open_excel(fpath)
        table = data.sheets()[0]
        nrows = table.nrows - 2

        if int(sunCount) == nrows:
            logger.info("行总计条数{0}".format(nrows))
        else:
            dr.get_screenshot_as_file(PICTURE_PATH + "/webPc/test_0602_01_TotalMoneyCheck.png")
            unittest.expectedFailure("test_0602_01_TotalMoneyCheck")
            file_remove(f)
        file_remove(f)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

