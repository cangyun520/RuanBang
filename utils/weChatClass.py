class WeChatPublic:
    """微信公共操作代码集合"""
    def start_weixin(self):
        """初始化配置微信应用"""
        self.desired_caps = {}
        desired_caps = self.desired_caps
        # 使用哪种移动平台。iOS, Android, orFirefoxOS
        desired_caps['platformName'] = 'Android'
        # 设备系统版本
        desired_caps['platformVersion'] = '6.0.0'
        # 启动哪种设备，是真机还是模拟器？iPhone Simulator, iPad Simulator, iPhone Retina 4-inch, Android Emulator, Galaxy S4, etc...
        desired_caps['deviceName'] = 'Android Emulator'
        # 待测试的app的java package
        desired_caps['appPackage'] = 'com.tencent.mm'
        # 待测试的app的Activity名字
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        # 解决无法输入中文问题
        self.desired_caps["unicodeKeyboard"] = "True"
        self.desired_caps["resetKeyboard"] = "True"
        # 使用哪种自动化引擎。appium（默认）还是Selendroid。api小于17使用Selendroid
        # self.desired_caps["automationName"] = "Selendroid"

        return self.desired_caps
