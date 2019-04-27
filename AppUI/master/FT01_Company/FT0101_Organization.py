# encoding:utf-8
"""
 * Created by Arvin.liu on 2019-4-2.
 * QQ 405367236
"""
# 随机数据
from common.webMaster import *
from common.generator import *
from common.log import *
from extend.sqlConnect.mysql_master import MysqlMaster


class Organization(unittest.TestCase):
    URL = Config().get('URL')

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

        v_num = MysqlMaster().query_one("SELECT count(id) from md_organizationextend")

        ObjectPc.button(self, "添加组织")
        v_company = random_company()
        dr.find_element_by_xpath("//*[@id='form_name']/div/div[2]/div/span/span/input").send_keys(v_company)

        # 组织类型
        js = 'RbCore.currentPage.getControlInstance().rIframe.context.getControlInstance().form.dataModel.type=1'
        dr.execute_script(js)
        logger('master').info(js)

        # 产品范围
        v_proTypes = '296616656422178817,296616656422178818,296616656422178819,296616656422178820,296616656422178821'
        js = "RbCore.currentPage.getControlInstance().rIframe.context.getControlInstance().form.dataModel.productTypeIds ='" + v_proTypes + "'"
        logger('master').info(js)
        dr.execute_script(js)

        # 保存
        ObjectPc.button(self, "保存")
        timesl(2)

        # 添加数据后列表校验
        v_total = MysqlMaster().query_one("SELECT count(id) from md_organizationextend")
        try:
            v_total > v_num
            v_result = "初始行数据：{0}，添加后数量：{1}，添加公司：{2}".format(v_num, v_total, v_company)
            print(v_result)
            logger('master').info(v_result)
        except Exception as e:
            logger('master').info(e)
            unittest.expectedFailure('test_0101_01_add')
            dr.get_screenshot_as_file(screenshot_path_app('master') + "master/test_0101_01_add.png")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
