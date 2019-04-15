# encoding:utf-8
"""
 * Created by Arvin.liu on 2018-9-6.
 * QQ 405367236
"""
from public.generator import *
from public.webClass import *


class PageRelease(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.sass_submit(self, "saas_zhzj", "15807146017", "0KW7EVJ8TT6GH6QL", "0KVZBIX14H05PEGQ61PK")
        # 打开菜单
        WebMenu.full_text(self, "基础数据", "外派人员管理")

    """外派人员管理-行数据添加"""
    def test_0101_01_add(self):
        """外派人员管理-行数据添加"""
        dr = self.driver
        SaaSPc.button(self, "新增")
        wid = SaaSPc.get_wid_body(self)
        _baseForm = wid+':baseForm$'

        _time = time.strftime("%m%d")

        # 供应商名称
        dr.find_element_by_id(_baseForm+'name').send_keys(random_name())
        # 身份证号
        dr.find_element_by_id(_baseForm + 'code').send_keys(random_ssn())
        #
        dr.find_element_by_id(_baseForm + 'salary').send_keys(random_int(5000, 25000))

        # dr.find_element_by_id(_baseForm + 'defaultStationId').click()
        # timesl(1)
        # _defaultStation = wid+':baseForm$defaultStationId$popup'
        # print(_defaultStation)
        # jobs = dr.find_elements_by_css_selector("#"+_defaultStation+">div>ul>li")
        # for i in jobs:
        #     print(i.text)
        # dr.find_element_by_id(_baseForm + 'ratepayerQualificationType').send_keys(Keys.ENTER)
        # 工资标准
        dr.find_element_by_id(_baseForm + 'salary').send_keys(random_int(5000, 30000))
        # 备注
        dr.find_element_by_id(_baseForm + 'remark').send_keys(random_paragraphs())

        SaaSPc.button(self, "保存")
        if "成功" in SaaSPc.get_tip(self):
            pass
            # SaaSPc.button(self, "关闭")
        else:
            dr.get_screenshot_as_file(PICTURE_PATH + "homePage/test_0101_01_add.png")
            unittest.expectedFailure("test_0101_01_add")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
