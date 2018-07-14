# encoding:utf-8
import pymssql
import types
"""
Created by Arvin.liu 15807146017
Date :2018-06-04.
"""
# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称


class Mysqldb:
    __db = None

    __config = {
        'host': "192.168.0.55",
        'port': 1433,
        'username': "sa",
        'password': "rb1234",
        'database': "sass_wwht",
        'charset': "utf8"
    }

    def __init__(self):
        self.__connect()

    def __del__(self):
        if(self.__db == None):
            self.__db.close()

    def __connect(self):
        if(self.__db == None):
            self.__db = pymssql.connect(
                host=self.__config['host'],
                port=self.__config['port'],
                user=self.__config['username'],
                password=self.__config['password'],
                database=self.__config['database'],
                charset=self.__config['charset']
            )
        return self.__db

    # 查询获取所有数据
    def query(self, _sql):
        cursor = self.__connect().cursor()
        try:
            cursor.execute(_sql)
            data = cursor.fetchall()
            # 提交到数据库执行
            self.__connect().commit()
        except:
            # 如果发生错误则回滚
            self.__connect().rollback()
            return False
        return data

    # 查询获取单行数据
    def query_one(self, _sql):
        cursor = self.__connect().cursor()
        try:
            cursor.execute(_sql)
            data = cursor.fetchone()
            # 提交到数据库执行
            self.__connect().commit()
        except:
            # 如果发生错误则回滚
            self.__connect().rollback()
            return False
        return data

    def query_dic(self, _sql_dic):
        if ('select' in _sql_dic.keys()):
            sql = "SELECT " + _sql_dic['select'] + " FROM " + _sql_dic['from'] + self.where(_sql_dic['where'])
            print(sql)
            return self.query(sql)
        elif ('insert' in _sql_dic.keys()):
            sql = "INSERT INTO " + _sql_dic['insert'] + self.quote(_sql_dic['domain_array'],
                                                                   type_filter=False) + " VALUES " + self.quote(
                _sql_dic['value_array'])
            print(sql)
            return self.query(sql)
        if ('delete' in _sql_dic.keys()):
            sql = "DELETE FROM " + _sql_dic['delete'] + self.where(_sql_dic['where'])
            print(sql)
            return self.query(sql)

    def where(self, _sql):
        if (isinstance(_sql, dict) == False):
            return " WHERE " + str(_sql)
        if (isinstance(_sql, dict)):
            _sql_dic = _sql
            s = " WHERE "
            index = 0
            for domain in _sql_dic:
                if (index == 0):
                    s += domain + "=" + str(_sql_dic[domain]) + " "
                    index += 1
                else:
                    s += "AND " + domain + "=" + str(_sql_dic[domain]) + " "
            return s

            # 为数组加上外括号，并拼接字符串

        def quote(self, _data_array, type_filter=True):
            s = "("
            index = 0
            if (type_filter):
                for domain in _data_array:
                    if (index == 0):
                        if (isinstance(domain, int)):
                            s += str(domain)
                        elif (isinstance(domain, str)):
                            s += "'" + domain + "'"
                        index += 1
                    else:
                        if (isinstance(domain, int)):
                            s += ", " + str(domain)
                        elif (isinstance(domain, str)):
                            s += ", " + "'" + domain + "'"
            else:
                for domain in _data_array:
                    if (index == 0):
                        s += str(domain)
                        index += 1
                    else:
                        s += ", " + domain
            return s + ")"

"""
参考  https://blog.csdn.net/leyounger/article/details/73277209
"""

if __name__ == "__main__":
    db = SqlServer()
    _sql = "SELECT * FROM wht_Contract"
    a= db.query_one(_sql)
    print(a)