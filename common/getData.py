# encoding='UTF-8'
import csv
import random
import time

from config import DATA_PATH


# 随机生成18位身份证号码
def get_idcard():
    """ 随机生成新的18为身份证号码 """
    arr = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    last = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' % (
        random.randint(10, 99),
        random.randint(1, 99),
        random.randint(1, 99),
        random.randint(t - 60, t - 18),
        random.randint(1, 12),
        random.randint(1, 28),
        random.randint(1, 999)
    )
    y = 0
    for i in range(17):
        y += int(x[i]) * arr[i]
    return '%s%s' % (x, last[y % 11])


# 获取姓名
def get_name():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[0]:
            if ii != " ":
                arr.append(i[0])
    return arr[random.randint(1, len(arr)-1)]


# 获取手机号码
def get_mobile():
    _iphone = random.choice(
        ['139', '188', '185', '136', '158', '151', '177']
    )+"".join(random.choice("0123456789") for i in range(8))
    return _iphone


# 获取邮箱号码
def get_email():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[2]:
            if ii != " ":
                arr.append(i[2])
    return arr[random.randint(1, len(arr)-1)]


# 获取电话
def get_tel():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[4]:
            if ii != " ":
                arr.append(i[4])
    return arr[random.randint(1, len(arr) - 1)]


# 获取英文名称
def get_englishname():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[3]:
            if ii != " ":
                arr.append(i[3])
    return arr[random.randint(1, len(arr) - 1)]


# 获取职位名称
def get_job():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[5]:
            if ii != " ":
                arr.append(i[5])
    return arr[random.randint(1, len(arr) - 1)]


# 获取公司名称
def get_company():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[6]:
            if ii != " ":
                arr.append(i[6])
    return arr[random.randint(1, len(arr) - 1)]


# 获取详细地址
def get_address():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[7]:
            if ii != " ":
                arr.append(i[7])
    return arr[random.randint(1, len(arr) - 1)]


# 获取高校名称
def get_university():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[8]:
            if ii != " ":
                arr.append(i[8])
    return arr[random.randint(1, len(arr) - 1)]


# 获取高校专业
def get_specialty():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[9]:
            if ii != " ":
                arr.append(i[9])
    return arr[random.randint(1, len(arr) - 1)]


# 获取中国人力资格证书
def get_certificate():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[10]:
            if ii != " ":
                arr.append(i[10])
    return arr[random.randint(1, len(arr) - 1)]


# 获取中国城市名称
def get_city():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[11]:
            if ii != " ":
                arr.append(i[11])
    return arr[random.randint(1, len(arr) - 1)]


# 获取中国人力职务名称
def get_position():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[12]:
            if ii != " ":
                arr.append(i[12])
    return arr[random.randint(1, len(arr) - 1)]


# 获取省份
def get_province():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[13]:
            if ii != " ":
                arr.append(i[13])
    return arr[random.randint(1, len(arr) - 1)]


# 获取姓氏
def get_surname():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[16]:
            if ii != " ":
                arr.append(i[16])
    return arr[random.randint(1, len(arr) - 1)]


# 获取中国少数民族名称
def get_nation():
    _data = csv.reader(open(DATA_PATH + '/cvs/basedata.csv', 'r'))
    arr = []
    for i in _data:
        for ii in i[0]:
            if ii != " ":
                arr.append(i[0])
    return arr[random.randint(1, len(arr) - 1)]


# 随机生成网址
def get_www():
    www = "www." + "".join(random.choice("abcdefghjklmnopqrst") for i in range(6)) + ".com"
    return www


# 获取开户银行名称
def get_bank():
    _data = csv.reader(open(DATA_PATH + ('/cvs/basedata.csv'), 'r'))
    arr = []
    for i in _data:
        for ii in i[14]:
            if ii != " ":
                arr.append(i[14])
    return arr[random.randint(1, len(arr) - 1)]


# 设置自定义字符串测试
def get_character(start, end):
    with open(DATA_PATH + '/text/character5K.txt', 'r', encoding='UTF-8') as data:
        _lines = data.read()
        character = _lines[start:end]
    return character


# 用切片去除字符串首尾空格
def get_trim(s):
    for i in range(len(s)):
        if s[0] == ' ':
            s = s[1:]
    for k in range(len(s)):
        if s[-1] == ' ':
            s = s[:-1]
    return s


# 测试
if __name__ == "__main__":
    print(get_idcard())
    print(get_name())
    print(get_mobile())
    print(get_email())
    print(get_tel())
    print(get_englishname())
    print(get_job())
    print(get_company())
    print(get_address())
    print(get_university())
    print(get_specialty())
    print(get_certificate())
    print(get_city())
    print(get_position())
    print(get_surname())
    print(get_nation())
    print(get_www())
    print(get_bank())
    print(get_character(6, 100))



"""
    With语句是什么？
    有一些任务，可能事先需要设置，事后做清理工作。对于这种场景，Python的with语句提供了一种非常方便的处理方式。一个很好的例子是文件处理，你需要获取一个文件句柄，从文件中读取数据，然后关闭文件句柄。
    如果不用with语句，代码如下：
    file = open("/tmp/foo.txt")
    data = file.read()
    file.close()
    这里有两个问题。一是可能忘记关闭文件句柄；二是文件读取数据发生异常，没有进行任何处理。下面是处理异常的加强版本：
    file = open("/tmp/foo.txt")
    try:
        data = file.read()
    finally:
        file.close()
    虽然这段代码运行良好，但是太冗长了。这时候就是with一展身手的时候了。除了有更优雅的语法，with还可以很好的处理上下文环境产生的异常。下面是with版本的代码：
    with open("/tmp/foo.txt") as file:
        data = file.read()
"""