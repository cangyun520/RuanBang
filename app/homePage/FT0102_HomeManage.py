# encoding:utf-8
from public.webClass import *
from public.config import *

_time = time.strftime("%m%d")


class HomeManag(unittest.TestCase):
    def setUp(self):
        # 指定浏览器
        self.driver = webdriver.Chrome()
        # 登录
        WebLogin.submit(self, "homePage", "0KPTYTUA7R0UQBR3P4IF")
        # 打开菜单
        WebMenu.full_text(self, "钉钉定制", "首页管理")

    """首页管理-行数据删除"""
    def test_0102_01_deleteGroup(self):
        """应收款情况-行数据删除"""
        dr = self.driver
        n = 0
        # num = 3     # 后续通过数据库查询获取值或者根据列表查询（考虑到外部不能访问数据）
        js = "return Rb.Pages.Page.s_pages['w0'].getControl('gridEditGroup').model.length;"
        num = dr.execute_script(js)
        try:
            while n < num:
                bs = dr.find_elements_by_css_selector(".rb-row-buttons>span.rb-row-button")
                for b in bs:
                    if b.text == "删除" and b.get_attribute("data-itemid") == "deleteGroup":
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

    """首页管理-行增加"""
    def test_0102_02_lineAdd(self):
        """首页管理-行增加"""
        dr = self.driver
        dr.find_element_by_xpath("//*[@id='w0:toolBarGroup']/div[1]/span[1]").click()
        # 获取新增的wid
        wid = SAASPc.get_wid_body(self)

        lpath = wid + ':baseForm$name'
        dr.find_element_by_xpath("//*[@id='" + lpath + "']/span[1]/input").send_keys("行自动化"+_time)

        ltb = wid + ':toolbar'
        dr.find_element_by_xpath("//*[@id='" + ltb + "']/div/span[1]").click()
        timesl(1)

        if "成功" in SAASPc.get_tip(self):
            dr.find_element_by_xpath("//*[@id='" + ltb + "']/div/span[2]").click()
        else:
            dr.get_screenshot_as_file(PICTURE_PATH + "homePage/test_0102_02_lineAdd.png")
            unittest.expectedFailure("test_0102_02_lineAdd")

    """首页管理-列新增（url）"""
    def test_0102_03_colAddUrl(self):
        """应收款情况-列新增（url）"""
        dr = self.driver
        # 选定特定行
        cells = dr.find_elements_by_class_name("dataCell")
        for i in cells:
            if i.text == "行自动化"+_time:
                i.click()
                break
        # 新增列-外部链接
        dr.find_element_by_xpath("//*[@id='w0:toolBarMetro']/div[1]/span[1]").click()
        # 进入到区块页面
        # 获取新增的wid
        wid = SAASPc.get_wid_body(self)

        # 类型
        _lx = wid + ':baseForm$type'
        dr.find_element_by_xpath("//*[@id='" + _lx + "']").send_keys("外部链接")
        dr.find_element_by_xpath("//*[@id='" + _lx + "']").send_keys(Keys.ENTER)

        # URL地址
        _url = wid + ':baseForm$path'
        _http = 'https://m.baidu.com/?tn=&from'
        _httpName = '百度一下'
        dr.find_element_by_xpath("//*[@id='" + _url + "']").send_keys(_http)

        # 列名称
        _lmc = wid + ':baseForm$name'
        dr.find_element_by_xpath("//*[@id='" + _lmc + "']").send_keys(_httpName)

        # 列名称隐藏
        _lmc_yc = wid + ':baseForm$hidden'
        dr.find_element_by_xpath("//*[@id='" + _lmc_yc + "']/span[2]").click()

        # 风格 钉钉应用风格
        _fg = wid + ':baseForm$style'
        dr.find_element_by_xpath("//*[@id='" + _fg + "']/span[2]").click()

        # 图片
        _log = DATA_PATH + "/img/log/baidu_logo.png"
        dr.find_element_by_id("metro_fileUpload").send_keys(_log)
        timesl(2)

        # 保存
        _save = wid + ':toolbar'
        dr.find_element_by_xpath("//*[@id='" + _save + "']/div/span[1]").click()

        if "成功" in SAASPc.get_tip(self):
            dr.find_element_by_xpath("//*[@id='" + _save + "']/div/span[2]").click()
        else:
            dr.get_screenshot_as_file(PICTURE_PATH + "homePage/test_0102_03_colAddUrl.png")
            unittest.expectedFailure("test_0102_03_colAddUrl")

        # 列保存
        dr.find_element_by_xpath("//*[@id='w0:toolBarMetro']/div[1]/span[2]").click()
        # 发布
        dr.find_element_by_xpath("//*[@id='w0:buttons']/div/span").click()
        try:
            SAASPc.button(self, "确认")
        except Exception as e:
            logger.info(e)
            dr.get_screenshot_as_file(PICTURE_PATH + "homePage/test_0102_03_colAddUrl.png")
            unittest.expectedFailure("test_0102_03_colAddUrl")

    """首页管理-列新增(页面)"""
    def test_0102_04_colAddPage(self):
        """应收款情况-列新增(页面)"""
        dr = self.driver
        # 选定特定行
        cells = dr.find_elements_by_class_name("dataCell")
        for i in cells:
            if i.text == "行自动化"+_time:
                i.click()
                break
        # 新增列-页面
        dr.find_element_by_xpath("//*[@id='w0:toolBarMetro']/div[1]/span[1]").click()
        # 进入到区块页面
        # 获取新增的wid
        wid = SAASPc.get_wid_body(self)
        # 类型
        _lx = wid + ':baseForm$type'
        dr.find_element_by_xpath("//*[@id='" + _lx + "']").send_keys("页面")
        timesl(1)
        dr.find_element_by_xpath("//*[@id='"+_lx+"']").send_keys(Keys.ENTER)
        timesl(2)
        # 页面列表
        js = "return Rb.Pages.Page.s_pages['"+wid+"'].getControl('gridPost').data;"
        # print(js)
        _list = dr.execute_script(js)
        for i in _list:
            if i['name'] == 'Python爬虫之'+_time:
                rd = i['_id']
                break
        # 选定指定行
        js2 = "return Rb.Pages.Page.s_pages['"+wid+"'].getControl('gridPost').selectedRow('"+rd+"')"
        dr.execute_script(js2)
        timesl(1)

        # 列名称隐藏
        _lmc_yc = wid + ':baseForm$hidden'
        dr.find_element_by_xpath("//*[@id='" + _lmc_yc + "']/span[2]").click()

        # 风格 钉钉应用风格
        _fg = wid + ':baseForm$style'
        dr.find_element_by_xpath("//*[@id='" + _fg + "']/span[2]").click()

        # 图片
        _log = DATA_PATH + "/img/log/selenium_logo.png"
        dr.find_element_by_id("metro_fileUpload").send_keys(_log)
        timesl(2)

        # 页面保存
        _save = wid + ':toolbar'
        dr.find_element_by_xpath("//*[@id='" + _save + "']/div/span[1]").click()

        if "成功" in SAASPc.get_tip(self):
            dr.find_element_by_xpath("//*[@id='" + _save + "']/div/span[2]").click()
        else:
            dr.get_screenshot_as_file(PICTURE_PATH + "homePage/test_0102_04_colAddPage.png")
            unittest.expectedFailure("test_0102_04_colAddPage")

        # 列保存
        dr.find_element_by_xpath("//*[@id='w0:toolBarMetro']/div[1]/span[2]").click()
        # 发布
        dr.find_element_by_xpath("//*[@id='w0:buttons']/div/span").click()
        try:
            SAASPc.button(self, "确认")
        except Exception as e:
            logger.info(e)
            dr.get_screenshot_as_file(PICTURE_PATH + "homePage/test_0102_04_colAddPage.png")
            unittest.expectedFailure("test_0102_04_colAddPage")

    """首页管理-行配置（高度，说明）"""
    def test_0102_06_lineSet(self):
        """应收款情况-行配置（高度，说明）"""
        dr = self.driver
        cells = dr.find_elements_by_class_name("dataCell")
        for i in cells:
            if i.get_attribute("data-id") == "rowHeight":
                i.click()
                dr.find_element_by_id("w0:gridEditGroup$rowHeight").send_keys(150)
        # 保存
        dr.find_element_by_xpath("//*[@id='w0:toolBarGroup']/div[1]/span[2]").click()
        # 发布
        dr.find_element_by_xpath("//*[@id='w0:buttons']/div/span").click()
        try:
            SAASPc.button(self, "确认")
        except Exception as e:
            logger.info(e)
            dr.get_screenshot_as_file(PICTURE_PATH + "homePage/test_0102_06_lineSet.png")
            unittest.expectedFailure("test_0102_06_lineSet")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
