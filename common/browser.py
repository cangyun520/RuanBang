import os
import time

from selenium import webdriver

from config import DRIVER_PATH, REPORT_PATH

# 可根据需要扩展
CHROMEDRIVER_PATH = DRIVER_PATH + '\cchromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\cchromedriver.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\cchromedriver.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome':CHROMEDRIVER_PATH, 'ie':IEDRIVER_PATH, 'phantomjs': PHANTOMJSDRIVER_PATH}

class UnSupportBrowserTypeError(Exception):
    pass

class Browser(object):
    def __init__(self, browser_type = 'chrom'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%' % ','.join(TYPES.keys()))
        self.driver = None


    def get(self, url, maximize_window=True, implicitly_wait=30):
        # 设置页面上隐形的智能等待时间30秒
        # 浏览器最大化
        self.driver = self.browser(executable_path = EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()