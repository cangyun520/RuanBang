# encoding:utf-8
"""
 * Created by Arvin.liu on 2018-9-6.
 * QQ 405367236
"""
from public.webClass import *
from public.config import *
# 随机数据
from public.generator import *


class Organization(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.master_login(self, "master_test", "user", "user123456")
        # 打开菜单
        WebMenu.top_full_text(self, "公司主数据")
        self.driver.find_element_by_id('/page/mdm/02/$Menu').click()
        self.driver.find_element_by_xpath("//*[@id='/page/mdm/02/$Menu']/li[1]").click()

    """管理组织-添加组织"""
    def test_0101_01_add(self):
        """管理组织-添加组织"""
        dr = self.driver
        SaaSPc.button(self, "添加组织")
        timesl(20)
        js = "RbCore.currentPage.getControlInstance().rIframe.context.getControlInstance().form.dataModel.type=1"
        dr.execute_script(js)


        '''所属板块
        295939592245350400 = 地产开发
        295939592312459264 = 物业服务
        295939592312459265 = 商业运营
        303505516171235328 = 医疗养老
        303505516171235329 = 海外业务
        '''
        data = '295939592245350400'
        js = "RbCore.currentPage.getControlInstance().rIframe.context.getControlInstance().form.dataModel.businessPlateId="+ data

        '''产品范围
        296616656422178816,高层
        296616656422178817,小高层
        296616656422178818,花园洋房
        296616656422178819,别墅
        296616656422178820产业园
        '''
        data = '296616656422178816,296616656422178817,296616656422178818,296616656422178819,296616656422178820'
        js = "RbCore.currentPage.getControlInstance().rIframe.context.getControlInstance().form.dataModel.productTypeIds="+ data
        dr.execute_script(js)

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
