# encoding:utf-8
from public.webClass import *
from public.config import *
import requests


class PageRelease(unittest.TestCase):
    def setUp(self):
        # 登录
        WebLogin.sass_submit(self, "saas_fuping", "15807146017", "0KU4PRXX007REPVJ", "0KU0S8N54X0ASRHG8K89")
        dr = self.driver
        cookie = dr.get_cookies()
        with open(DATA_PATH + '/cookie/fuping.txt', 'w') as f:
            f.write(cookie)

    """页面保留缓存"""
    def test_0101_01_deleteGroup(self):
        with open(DATA_PATH + '/cookie/fuping.txt', 'rb') as f:
            cookie = f.read()
        print(cookie)

        url = "http://192.168.0.55:9004/service/common/login"
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