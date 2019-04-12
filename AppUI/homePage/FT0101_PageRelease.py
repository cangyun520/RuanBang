# encoding:utf-8
from public.webClass import *

from common.config import *


class PageRelease(unittest.TestCase):
    def setUp(self):
        # 登录
        WebLogin.submit(self, "homePage", "0KPTYTUA7R0UQBR3P4IF")
        # 打开菜单
        WebMenu.full_text(self, "页面管理", "页面发布")

    """页面发布-行数据删除"""
    def test_0101_01_deleteGroup(self):
        """页面发布-行数据删除"""
        dr = self.driver
        wid = SaaSPc.get_wid(self)

        # 页面分类数据列表
        js = "return Rb.Pages.Page.s_pages['" + wid + "'].getControl('leftGrid').data;"
        # 记录运行日志
        logger.info(js)
        _list = dr.execute_script(js)
        for i in _list:
            if i['name'] == '自动化测试':
                rd = i['_id']
                break
        # 选定指定行
        js = "return Rb.Pages.Page.s_pages['" + wid + "'].getControl('leftGrid').selectedRow('" + rd + "')"
        dr.execute_script(js)
        timesl(1)

        # 删除页面管理数据
        n = 0
        js = "return Rb.Pages.Page.s_pages['" + wid + "'].getControl('rightGrid').data.length;"
        num = dr.execute_script(js)
        try:
            while n < num:
                bs = dr.find_elements_by_css_selector(".rb-row-buttons>span.rb-row-button")
                for b in bs:
                    if b.text == "删除" and b.get_attribute("data-itemid") == "del":
                        b.click()
                        # 删除确认
                        qs = dr.find_elements_by_css_selector(".rb-button.active")
                        for a in qs:
                            if a.get_attribute("data-id") == "ok":
                                a.click()
                                timesl(1)
                                break
                        break
                n += 1
        except Exception as e:
            logger.info(e)
            dr.get_screenshot_as_file(PICTURE_PATH + "homePage/test_0102_01_deleteGroup.png")
            unittest.expectedFailure("test_0102_01_deleteGroup")

    """页面发布-行数据添加"""
    def test_0101_02_pageAdd(self):
        """页面发布-行数据添加"""
        dr = self.driver
        wid = SaaSPc.get_wid(self)
        _time = time.strftime("%m%d")

        # 页面分类数据列表
        _list = SaaSPc.get_list_value(self, wid, "leftGrid")
        for i in _list:
            if i['name'] == '自动化测试':
                rd = i['_id']
                break
        # 选定指定行
        js = "return Rb.Pages.Page.s_pages['"+wid+"'].getControl('leftGrid').selectedRow('"+rd+"')"
        dr.execute_script(js)
        dr.find_element_by_xpath("//*[@id='w0:rightToolbar']/div[1]/span[1]").click()
        timesl(1)
        # 文章发布页面
        wid = SaaSPc.get_wid(self)
        _title = "Python爬虫之"+_time
        # 标题
        dr.find_element_by_xpath("//*[@id='"+wid+":baseForm$title']/span[1]/input").send_keys(_title)
        # 页面分类
        _ymfl = wid + ':baseForm$categoryId'
        dr.find_element_by_xpath("//*[@id='"+_ymfl+"']").send_keys("自动化")
        dr.find_element_by_xpath("//*[@id='"+_ymfl+"']").send_keys(Keys.ENTER)
        # 正文内容
        dr.find_element_by_id("edui1_iframeholder").click()
        dr.find_element_by_id("ueditor_0").send_keys(get_character(100, 1200))
        timesl(2)
        # 发布状态
        _fbzt = wid + ':baseForm$state'
        dr.find_element_by_xpath("//*[@id='"+_fbzt+"']/span[2]").click()

        # 保存
        _save = wid + ':toolbar'
        dr.find_element_by_xpath("//*[@id='"+_save+"']/div/span[1]").click()
        timesl(0.5)

        if "成功" in SaaSPc.get_tip(self):
            dr.find_element_by_xpath("//*[@id='"+_save+"']/div/span[2]").click()
        else:
            dr.get_screenshot_as_file(PICTURE_PATH + "homePage/test_0101_02_pageAdd.png")
            unittest.expectedFailure("test_0101_02_pageAdd")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
