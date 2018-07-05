# encoding:utf-8
"""
Created by Arvin.liu 15807146017
Date :2018-06-08.
"""
import unittest


class Count:
    def __index__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b


# noinspection PyArgumentList,PyArgumentList
class TestCount(unittest.TestCase):
    def setUp(self):
        print('test start')

    # noinspection PyArgumentList,PyArgumentList
    def test_add(self):
        try:
            # noinspection PyArgumentList,PyArgumentList
            j = Count(2, 3)
            self.assertEqual(j.add(), 5)
        except AssertionError as msg:
            print(msg)
        else:
            print('Test pass')

    def tearDown(self):
        print('test end')

if __name__ == '__main__':
    unittest.main()