# encoding:utf-8
"""
 * Created by Arvin.liu on 2018-7-18.
 * QQ 405367236
"""
from public.webClass import *


class PollsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        base_url = 'http://192.168.0.55:9004/login'
        self.driver.get(base_url)

    def fuping(self):
        dr = self.driver
        js_path = DATA_PATH + '/js/fuping.js'
        with open(js_path, 'r', encoding='utf-8') as f:
            line = f.read()
            print(line)
        print(dr.execute_script(line))
        timesl(2)

    def tearDown(self):
        pass

    # def test_get_poll_index(self):
    #     r = requests.get(self.base_url)
    #     code = r.status_code
    #     self.assertEqual(code, 200)
    #
    # def test_get_poll_question(self):
    #     r = requests.get(self.base_url + "/1/")
    #     code = r.status_code
    #     text = r.text
    #     self.assertEqual(code, 200)
    #     self.assertIn("3", text)


if __name__ == "__main__":
    unittest.main()


# 接口-豆瓣查询
class Douban(object):
    url = "https://api.douban.com/v2/book/search"

    querystring = {"q": u"python接口测试"}

    headers = {
        'Cache-Control': "no-cache",
        # 'Postman-Token': "56997102-988b-40e2-9a9e-e9d410025bfe"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.status_code)
    # for i in response:
    #     print(response.text)
    cooike = response.cookies
    for i in cooike:
        print(i)
