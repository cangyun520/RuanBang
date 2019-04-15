# encoding:utf-8
"""
Created by Arvin.liu 15807146017
Date :2018-08-02.
"""
import os

from config import DOWN_PATH


# 查找某类型文件
def file_find(t, _dir=DOWN_PATH):
    L = []
    t = '.'+t
    for root, dirs, files in os.walk(_dir):
        for file in files:
            if os.path.splitext(file)[1] == t:
                L.append(file)
    return L


# 获取指定文件绝对路径
def file_path(file, _dir=DOWN_PATH):
    P = None
    for root, dirs, files in os.walk(_dir):
        for i in files:
            if i == file:
                P = root + file
                break
    return P


# 删除指定文件
def file_remove(file, _dir=DOWN_PATH):
    file = _dir+file
    if os.path.exists(file):
        os.remove(file)
    else:
        print('没有发现该文件{0}'.format(file))


if __name__ == '__main__':
    # a = file_find("xlsx")
    # print(a)
    # file_remove("签约明细(2018-08-03) (4).xlsx")
    p = file_path("签约明细(2018-08-03) (4).xlsx")
    print(p)


"""
split()和os.path.split()两个函数，他们的主要区别可以概括为一个从前往后搜索字符串，后者则是从后往前搜索 '.'（reverse search）。
os.path.splitext()更多的运用在了搜索文件路径（path）和文件的扩展名（ext)，这两个组合在一起构成了完整的路径，如果使用正常的split()函数来获取扩展名，那么效率是很低的。
os.walk()遍历目录中所有文件
"""