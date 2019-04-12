# encoding:utf-8
"""
 * Created by Arvin.liu on 2018-9-6.
 * QQ 405367236
"""
from public.generator import *
from public.webClass import *

from common.config import *


class PageRelease(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.sass_submit(self, "saas_zhzj", "15807146017", "0KW7EVJ8TT6GH6QL", "0KVZBIX14H05PEGQ61PK")
        # 打开菜单
        WebMenu.full_text(self, "基础数据", "供应商管理")

    """供应商管理-行数据添加"""
    def test_0101_01_add(self):
        """供应商管理-行数据添加"""
        dr = self.driver
        SaaSPc.button(self, "新增")
        wid = SaaSPc.get_wid(self)
        _baseForm = wid+':baseForm$'
        print(_baseForm)
        _time = time.strftime("%m%d")

        # 供应商名称
        dr.find_element_by_id(_baseForm+'name').send_keys(random_province()+random_company())
        dr.find_element_by_id(_baseForm + 'shortName').send_keys(random_company_prefix())
        # 供应商编码
        dr.find_element_by_id(_baseForm + 'code').send_keys('GYS-'+random_ssn())
        # 一般纳税人
        dr.find_element_by_id(_baseForm + 'ratepayerQualificationType').send_keys('一般纳税人')
        dr.find_element_by_id(_baseForm + 'ratepayerQualificationType').send_keys(Keys.ENTER)
        # 纳税人识别号
        dr.find_element_by_id(_baseForm + 'ratepayerCode').send_keys(random_str(15, 18))
        # 法人
        dr.find_element_by_id(_baseForm + 'legalPerson').send_keys(random_name())
        # 备注
        dr.find_element_by_id(_baseForm + 'remark').send_keys(random_paragraphs())
        # 联系人信息Tab数据编辑
        _gridEdit = wid + ':gridEdit1$'
        js = "return Rb.Pages.Page.s_pages['" + wid + "'].getControl('gridEdit1').modifyCell('r0','name')"
        dr.execute_script(js)
        dr.find_element_by_id(_gridEdit + 'name').send_keys(random_name())
        # 联系电话
        js = "return Rb.Pages.Page.s_pages['" + wid + "'].getControl('gridEdit1').modifyCell('r0','tel')"
        dr.execute_script(js)
        dr.find_element_by_id(_gridEdit + 'tel').send_keys(random_phone_number())
        # 是否默认
        js = "return Rb.Pages.Page.s_pages['" + wid + "'].getControl('gridEdit1').modifyCell('r0','isDefault')"
        dr.execute_script(js)
        # dr.find_element_by_id(_gridEdit + 'isDefault_r0').click()
        dr.find_element_by_xpath("//*[@id='" + _gridEdit + "isDefault_r0']/span").click()
        # 备注
        js = "return Rb.Pages.Page.s_pages['" + wid + "'].getControl('gridEdit1').modifyCell('r0','remark')"
        dr.execute_script(js)
        dr.find_element_by_id(_gridEdit + 'remark').send_keys(random_sentence())

        # 开户行信息Tab数据编辑
        SaaSPc.tab_nav(self, '开户行信息')
        _gridEdit = wid + ':gridEdit2$'
        js = "return Rb.Pages.Page.s_pages['" + wid + "'].getControl('gridEdit2').modifyCell('r0','accountNumber')"
        dr.execute_script(js)
        dr.find_element_by_id(_gridEdit + 'accountNumber').send_keys(random_card_number())
        # 开户行
        js = "return Rb.Pages.Page.s_pages['" + wid + "'].getControl('gridEdit2').modifyCell('r0','openingBank')"
        dr.execute_script(js)
        dr.find_element_by_id(_gridEdit + 'openingBank').send_keys("工行")
        # 开户支行
        js = "return Rb.Pages.Page.s_pages['" + wid + "'].getControl('gridEdit2').modifyCell('r0','subbranchBank')"
        dr.execute_script(js)
        dr.find_element_by_id(_gridEdit + 'subbranchBank').send_keys("软件园支行")
        # 是否默认
        js = "return Rb.Pages.Page.s_pages['" + wid + "'].getControl('gridEdit2').modifyCell('r0','isDefault')"
        dr.execute_script(js)
        # dr.find_element_by_id(_gridEdit + 'isDefault_r0').click()
        dr.find_element_by_xpath("//*[@id='" + _gridEdit + "isDefault_r0']/span").click()
        # 备注
        js = "return Rb.Pages.Page.s_pages['" + wid + "'].getControl('gridEdit2').modifyCell('r0','remark')"
        dr.execute_script(js)
        dr.find_element_by_id(_gridEdit + 'remark').send_keys(random_sentence())

        SaaSPc.button(self, "保存")
        if "成功" in SaaSPc.get_tip(self):
            SaaSPc.button(self, "返回")
        else:
            dr.get_screenshot_as_file(PICTURE_PATH + "homePage/test_0101_02add.png")
            unittest.expectedFailure("test_0101_02add")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
