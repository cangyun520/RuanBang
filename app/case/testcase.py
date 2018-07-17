import unittest
from public.HTMLTestRunner_PY3 import HTMLTestRunner
from public.config import REPORT_PATH


class TestHTMLTestRunnerPY3(unittest.TestCase):
    """ 测试PY3 HTMLTESTRUNNER """
    def test_py3_success(self):
        """ 此用例成功 """
        self.assertEqual(1+1, 2)

    def test_py3_fail(self):
        """ 此用例失败 """
        self.assertEqual(1+1, 3)


class TestHTML(unittest.TestCase):
    """ 测试PY3 HTMLTESTRUNNER 2 """
    def test_html_success(self):
        """ 此用例成功 """
        for i in range(5):
            with self.subTest(data=i):  # 注意这里subTest的用法
                self.assertEqual(1+2, 3)


# class TestError(unittest.TestCase):
#     """ 测试PY3 HTMLTESTRUNNER ERROR 3 """
#     def test_error(self):
#         """ 此用例出错 """
#         self.assertEqual(1/0, 1)


if __name__ == '__main__':
    import os
    report = os.path.join(REPORT_PATH + '/report.html')
    st = unittest.TestSuite()
    st.addTests([TestHTMLTestRunnerPY3('test_py3_success'), TestHTMLTestRunnerPY3('test_py3_fail'),
                 TestHTML('test_html_success')])
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='示例测试报告', description='执行人：灰蓝')
        runner.run(st)