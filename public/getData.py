import random
import time
import csv
from public.config import propath


# 随机生成18位身份证号码
def fun_idcard():
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
def data_name():
    v_data = csv.reader(open(propath()+'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[0]:
            if ii != " ":
                arr.append(i[0])
    return arr[random.randint(1, len(arr)-1)]


# 获取手机号码
def data_mobile():
    v_iphone = random.choice(
        ['139', '188', '185', '136', '158', '151', '177']
    )+"".join(random.choice("0123456789") for i in range(8))
    return v_iphone


# 获取邮箱号码
def data_email():
    v_data = csv.reader(open(propath()+'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[2]:
            if ii != " ":
                arr.append(i[2])
    return arr[random.randint(1, len(arr)-1)]


# 获取电话
def data_tel():
    v_data = csv.reader(open(propath() + 'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[4]:
            if ii != " ":
                arr.append(i[4])
    return arr[random.randint(1, len(arr) - 1)]


# 获取英文名称
def data_englishname():
    v_data = csv.reader(open(propath() + 'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[3]:
            if ii != " ":
                arr.append(i[3])
    return arr[random.randint(1, len(arr) - 1)]


# 获取职位名称
def data_job():
    v_data = csv.reader(open(propath()+'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[5]:
            if ii != " ":
                arr.append(i[5])
    return arr[random.randint(1, len(arr) - 1)]


# 获取公司名称
def data_company():
    v_data = csv.reader(open(propath()+'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[6]:
            if ii != " ":
                arr.append(i[6])
    return arr[random.randint(1, len(arr) - 1)]


# 获取详细地址
def data_address():
    v_data = csv.reader(open(propath()+'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[7]:
            if ii != " ":
                arr.append(i[7])
    return arr[random.randint(1, len(arr) - 1)]


# 获取高校名称
def data_university():
    v_data = csv.reader(open(propath()+'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[8]:
            if ii != " ":
                arr.append(i[8])
    return arr[random.randint(1, len(arr) - 1)]


# 获取高校专业
def data_specialty():
    v_data = csv.reader(open(propath()+'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[9]:
            if ii != " ":
                arr.append(i[9])
    return arr[random.randint(1, len(arr) - 1)]


# 获取中国人力资格证书
def data_certificate():
    v_data = csv.reader(open(propath()+'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[10]:
            if ii != " ":
                arr.append(i[10])
    return arr[random.randint(1, len(arr) - 1)]


# 获取城市
def data_city():
    v_data = csv.reader(open(propath()+'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[11]:
            if ii != " ":
                arr.append(i[11])
    return arr[random.randint(1, len(arr) - 1)]


# 获取中国人力职务名称
def data_position():
    v_data = csv.reader(open(propath()+'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[12]:
            if ii != " ":
                arr.append(i[12])
    return arr[random.randint(1, len(arr) - 1)]


# 获取省份
def data_province():
    v_data = csv.reader(open(propath()+'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[13]:
            if ii != " ":
                arr.append(i[13])
    return arr[random.randint(1, len(arr) - 1)]


# 获取姓氏
def data_surname():
    v_data = csv.reader(open(propath() + 'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[16]:
            if ii != " ":
                arr.append(i[16])
    return arr[random.randint(1, len(arr) - 1)]


# 获取中国少数民族名称
def data_nation():
    v_data = csv.reader(open(propath() + 'data/cvs/nation.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[0]:
            if ii != " ":
                arr.append(i[0])
    return arr[random.randint(1, len(arr) - 1)]


# 随机生成网址
def data_www():
    v_www = "www." + "".join(random.choice("abcdefghjklmnopqrst") for i in range(6)) + ".com"
    return v_www


# 获取自定义字符串测试
def data_character(start, end):
    write_file = open(propath() + 'data/character5K.txt', 'r')
    v_lines = write_file.read()
    v_input = v_lines[start:end]
    return v_input


# 获取SQL语句
def data_sql(filename):
    write_file = open(propath() + 'data/sql/' + filename, 'r')
    """
    .read()         读取整个文件
    .readline()     读取一行
    .readlines()    读取所有行的
    """
    v_lines = write_file.read()
    return v_lines


# 获取开户银行名称
def data_bank():
    v_data = csv.reader(open(propath()+'data/cvs/basedata.csv', 'r'))
    arr = []
    for i in v_data:
        for ii in i[14]:
            if ii != " ":
                arr.append(i[14])
    return arr[random.randint(1, len(arr) - 1)]