# encoding:utf-8
import requests
from common.webClass import *


class PageRelease(unittest.TestCase):
    def setUp(self):
        # 登录
        WebLogin.sass_submit(self, "manage", "刘朗洲", "YUANDINGYUN", "368739960423059456")
        dr = self.driver
        cookie = dr.get_cookies()
        with open(DATA_PATH + '/cookie/fuping.txt', 'w') as f:
            f.write(cookie)

    """页面保留缓存"""
    def test_0101_01_deleteGroup(self):
        with open(DATA_PATH + '/cookie/fuping.txt', 'rb') as f:
            cookie = f.read()
        print(cookie)

        url = "http://platform.yuandingyun.vip/?_t=1585643718668#/manage/8c2b76ev"
        querystring = {"data": 'value'}
        headers = {
            'cookie'
            'Cache-Control': "no-cache",
            # 'Postman-Token': "56997102-988b-40e2-9a9e-e9d410025bfe"
        }

        response = requests.request("POST", url, headers=headers, params=querystring)

        print(response.status_code)
        # for i in response:
        #     print(response.text)
        cooike = response.cookies
        for i in cooike:
            print(i)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()