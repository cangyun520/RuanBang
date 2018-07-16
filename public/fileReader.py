# encoding:utf-8
"""
Created by Arvin.liu 15807146017
Date :2018-06-15.
"""
import yaml
import os


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
