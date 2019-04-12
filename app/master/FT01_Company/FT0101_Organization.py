# encoding:utf-8
"""
 * Created by Arvin.liu on 2019-4-2.
 * QQ 405367236
"""
from public.webMaster import *
from public.config import *
# 随机数据
from public.generator import *


class Organization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.master_login(self, "master_test", "user", "user123456")
        # 打开菜单
        MenuOpen.menu_top_full(self, "公司主数据")
        self.driver.find_element_by_xpath("//*[@id='/page/mdm/02/$Menu']/li[1]").click()

    """管理组织-添加组织"""
    def test_0101_01_add(self):
        """管理组织-添加组织"""
        dr = self.driver
        # 选择 武汉光谷地产股份有限公司 自动化数据全部添加到这个公司
        v_tree = dr.find_elements_by_class_name("ant-tree-title")
        for i in v_tree:
            if "光谷地产" in i.text:
                i.click()
                break

        v_num = dr.find_elements_by_css_selector(".ant-table-tbody")[0].find_elements_by_css_selector("tr")
        v_num = len(v_num)

        ObjectPc.button(self, "添加组织")
        v_company = random_company()
        dr.find_element_by_xpath("//*[@id='form_name']/div/div[2]/div/span/span/input").send_keys(v_company)

        # 组织类型
        js = "RbCore.currentPage.getControlInstance().rIframe.context.getControlInstance().form.dataModel.type=1"
        dr.execute_script(js)
        logger.info(js)

        # 产品范围
        dr.find_element_by_xpath("//*[@id='form_productTypeIds']/div/div[2]/div/span/div/div/div").click()
        v_proTypes = dr.find_elements_by_class_name("ant-select-dropdown-menu-item")
        m = 5
        n = 0
        while n < m:
            v_proTypes[n].click()
            n += 1
        timesl(1)

        # 保存
        ObjectPc.button(self, "保存")
        timesl(2)

        # 添加数据后列表校验
        v_total = dr.find_elements_by_css_selector(".ant-table-tbody")[0].find_elements_by_css_selector("tr")
        v_total = len(v_total)
        try:
            v_total > v_num
            print("初始行数据：{0}，添加后数量：{1}，添加公司：{2}".format(v_num, v_total, v_company))
        except Exception as e:
            logger.info(e)
            unittest.expectedFailure('test_0101_01_add')
            dr.get_screenshot_as_file(PICTURE_PATH + "master/test_0101_01_add.png")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
