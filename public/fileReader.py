# encoding:utf-8
"""
Created by Arvin.liu 15807146017
Date :2018-06-15.
"""
import yaml
import os
from xlrd import open_workbook


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileExistsError("配置文件不存在")
        self._data = None

    # Python内置的 @ property装饰器就是负责把一个方法变成属性调用
    @property
    def data(self):
        # 如果是第一次调用打他，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                # load后是个generator，用list组织成列表
                self._data = list(yaml.safe_load_all(f))
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader(object):
    """
    读取Excel文件中的内容。返回list
    如：
    Excel中内容为：
    A |B |C
    A1|C2|C1
    A2|B2|c3
    如果 print(ExcelReader(excel,title_line = True).data),输出结果：
        [{A:A1,B:B1,C:C1},{A:A2,B:B2,C:C2}]
    如果 print（ExcelReader（Excel，title_line=False).data),输出结果:
        [[A,B,C],[A1,B1,C1],[A2,B2,C2]]

    可以指定sheet，通过index或者name：
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """

    def __init__(self, excel, sheet=0, title_line=True):
        """
        未实例化时，运行程序，构造方法没有运行
        """
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('Excel文件不存在')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            # title_line参数，用来声明是否在excel表格里有标题行，如果有标题行，返回dict列表，否则返回list列表
            if self.title_line:
                title = s.row_values(0)     # 默认首行为title
                for col in range(1, s.nrows):
                    # 依次遍历其余行，与首行组成dictionary，拼到self._data中
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    # 遍历所有行，拼到self._data中
                    self._data.append(s.row_values(col))
        return self._data

if __name__ == '__main__':
    y = "E:\PythonTest\RuanBang\config\config.yml"

    reader = YamlReader(y)
    for i in reader.data:
        print(i)

    e = "E:\PythonTest\RuanBang\data\excel\\basedata.xlsx"

    reader = ExcelReader(e, title_line=False)
    for i in reader.data:
        print(i)
