# encoding:utf-8
"""
Created by Arvin.liu 15807146017
Date :2018-06-05.
"""
import yaml
import os


class YamlReader(object):
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在')
        self._data = None

    @property
    # Python内置的 @ property装饰器负责把一个方法变成属性调用
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                # load后是个generator，用list组织成列表
                self._data = list(yaml.safe_load_all(f))
        return self._data
