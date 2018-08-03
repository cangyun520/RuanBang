# encoding:utf-8
"""
 * Created by Arvin.liu on 2018-8-3.
 * QQ 405367236
"""
import xlrd, sys, xdrlib
from public.downFile import *


def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e)


# 根据索引获取Excel表格中的数据
# 参数：file: Excel文件路径
# colnameindex: 表头列名所在行的索引
# by_index: 表的索引

def excel_table_byindex(file, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]     # 默认第一个sheet页
    # 获取行数和列数
    nrows = table.nrows
    ncols = table.ncols
    for i in range(0, nrows):
        rowValue = table.row_values(i)
        print(rowValue)


if __name__ == '__main__':
    file = file_path("签约明细(2018-08-03).xlsx")
    a = excel_table_byindex(file)
    print(a)
