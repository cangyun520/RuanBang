# encoding:utf-8
"""
Created by Arvin.liu 15807146017
Date :2018-06-15.
"""
import yaml
import os
from xlrd   import open_workbook


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

