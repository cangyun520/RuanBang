# encoding:utf-8
"""
 * Created by Arvin.liu on 2018-9-6.
 * QQ 405367236
"""
from public.generator import *
from public.webClass import *

from common.config import *


class Certification(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.sass_submit(self, "saas_zhzj", "15807146017", "0KW7EVJ8TT6GH6QL", "0KVZBIX14H05PEGQ61PK")
        # 打开菜单
        WebMenu.full_text(self, "证照管理", "资格证管理")

    """资格证管理-行数据添加"""
    def test_0203_01_add(self):
        """资格证管理-行数据添加"""
        dr = self.driver
        SaaSPc.button(self, "新增")
        wid = SaaSPc.get_wid(self)
        baseForm = wid+':baseForm$'
        # _time = time.strftime("%m%d")
        # 编号
        dr.find_element_by_id(baseForm + 'code').send_keys(random_ssn())
        # 证件类别
        dr.find_element_by_id(baseForm+'certificationTypeId').click()
        _id = "baseForm$certificationTypeId"
        _name = SaaSPc.selectButton(self, wid, _id)
        # 持证人姓名
        dr.find_element_by_id(baseForm + 'holderName').send_keys(random_name())
        # 联系电话
        dr.find_element_by_id(baseForm + 'holderTel').send_keys(random_phone_number())
        # 使用费用
        dr.find_element_by_id(baseForm + 'price').send_keys(random_int(1000, 5000))
        # 备注
        dr.find_element_by_id(baseForm + 'remark').send_keys(random_paragraphs())

        SaaSPc.button(self, "保存")
        if "成功" in SaaSPc.get_tip(self):
            print("当前添加的证书是：{0}".format(_name))
        else:
            dr.get_screenshot_as_file(PICTURE_PATH + "homePage/test_0203_01_add.png")
            unittest.expectedFailure("test_0203_01_add")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
