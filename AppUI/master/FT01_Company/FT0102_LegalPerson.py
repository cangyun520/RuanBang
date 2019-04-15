# encoding:utf-8
"""
 * Created by Arvin.liu on 2019-4-2.
 * QQ 405367236
"""
# 随机数据
from common.generator import *
from common.webMaster import *


class LegalPerson(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.master_login(self, "master_test", "user", "user123456")
        # 打开菜单
        MenuOpen.menu_top_full(self, "公司主数据")
        self.driver.find_element_by_xpath("//*[@id='/page/mdm/02/$Menu']/li[6]").click()

    """管理组织-法人公司"""
    def test_0102_01_add(self):
        """管理组织-添加组织"""
        dr = self.driver
        # 选择 武汉光谷地产股份有限公司 自动化数据全部添加到这个公司
        v_tree = dr.find_elements_by_class_name("ant-tree-title")
        for i in v_tree:
            if "光谷地产" in i.text:
                i.click()
                break
            timesl(1)

        v_num = dr.find_elements_by_css_selector(".ant-table-tbody")[0].find_elements_by_css_selector("tr")
        v_num = len(v_num)

        ObjectPc.button(self, "添加公司")
        # 统一社会信用代码
        v_card = random_credit_card()
        dr.find_element_by_xpath("//*[@id='form_creditCode']/div/div[2]/div/span/span/input").send_keys(v_card)
        # 企业名称
        v_company = random_company()
        dr.find_element_by_xpath("//*[@id='form_name']/div/div[2]/div/span/span/input").send_keys(v_company)
        # 类型
        js = "RbCore.currentPage.getControlInstance().form.dataModel.businessTypeId='295939592316653568';"
        dr.execute_script(js)
        logger.info(js)
        # 住所
        dr.find_element_by_xpath("//*[@id='form_address']/div/div[2]/div/span/span/input").send_keys(random_address())
        # 法定代表人
        dr.find_element_by_xpath("//*[@id='form_legalPerson']/div/div[2]/div/span/span/input").send_keys(random_name())
        # 注册资本
        dr.find_element_by_xpath("//*[@id='form_registeredCapital']/div/div[2]/div/span/div/div[2]/input").send_keys(random_int(10,1000000))
        # 成立日期
        # dr.find_element_by_xpath("//*[@id='form_establishmentDate']/div/div[2]/div/span/span/input").send_keys(random_past_date())
        # 经营范围
        dr.find_element_by_xpath("//*[@id='form_businessScope']/div/div[2]/div/span/textarea").send_keys()
        # 公司简称
        v_company_short = v_company.split('有')
        dr.find_element_by_xpath("//*[@id='form_shortName']/div/div[2]/div/span/span/input").send_keys(v_company_short)
        # 公司英文名称
        dr.find_element_by_xpath("//*[@id='form_englishName']/div/div[2]/div/span/span/input").send_keys(random_str(5, 20))
        # 注册币种
        js = "RbCore.currentPage.getControlInstance().form.dataModel.registeredCurrencyId='295991362757726209';"
        dr.execute_script(js)
        logger.info(js)

        # 保存
        ObjectPc.button(self, "完成")
        timesl(2)

        # 添加数据后列表校验
        v_total = dr.find_elements_by_css_selector(".ant-table-tbody")[0].find_elements_by_css_selector("tr")
        v_total = len(v_total)
        try:
            v_total > v_num
            print("初始行数据：{0}，添加后数量：{1}，法人公司：{2}".format(v_num, v_total, v_company))
        except Exception as e:
            logger.info(e)
            unittest.expectedFailure('test_0102_01_add')
            dr.get_screenshot_as_file(PICTURE_PATH + "master/test_0102_01_add.png")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
