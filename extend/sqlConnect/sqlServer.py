# encoding:utf-8
import pymssql

"""
Created by Arvin.liu 15807146017
Date :2018-06-14.

安装pymssql包  
    https://blog.csdn.net/amoscn/article/details/78215641
封装sqlserver增删改查常用方法  
    https://blog.csdn.net/u012935755/article/details/50178251
"""


# sqlserver 常用基本的增删改查 封装
class Sqlserverdb(object):
    _db = None

    # host    数据库服务器名称或IP
    # user      用户名
    # password  密码
    # database  数据库名称

    _config = {
        'host': "192.168.0.55",
        'port': 1433,
        'username': "sa",
        'password': "rb1234",
        'database': "sass_wwht",
        'charset': "utf8"
    }

    # 数据库连接
    def __connect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if(self._db == None):
            self._db = pymssql.connect(
                host=self._config['host'],
                port=self._config['port'],
                user=self._config['username'],
                password=self._config['password'],
                database=self._config['database'],
                charset=self._config['charset']
            )
        con = self._db
        if not con:
            raise (NameError, "数据库连接失败")
        else:
            return con

    # 获取查询所有结果
    def query(self, sql):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.__connect().cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except pymssql.Error as e:
            print("pymssql Error:%s" % e)
        finally:
            cursor.close()
            self.__connect().close()

    # 获取查询所有结果
    # noinspection PyPep8Naming
    def queryOne(self, sql):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.__connect().cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
        except pymssql.Error as e:
            print("pymssql Error:%s" % e)
        finally:
            cursor.close()
            self.__connect().close()

    # 不带参数的更新方法
    def update(self, sql):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.__connect().cursor()
        try:
            dosql = cursor.execute(sql)
            self.__connect().commit()
            return dosql
        except pymssql.Error as e:
            self.__connect().rollback()
            print("pymssql Error:%s" % e)
        finally:
            cursor.close()
            self.__connect().close()

    # 带参数的更新方法,eg:sql='insert into pythontest values(%s,%s,%s,now()',params=(6,'C#','good book')
    # noinspection PyPep8Naming
    def updateByParam(self, sql, params):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.__connect().cursor()
        try:
            dosql = cursor.execute(sql, params)
            self.__connect().commit()
            return dosql
        except pymssql.Error as e:
            self.__connect().rollback()
            print("pymssql Error:%s" % e)
        finally:
            cursor.close()
            self.__connect().close()

if __name__ == "__main__":
    # 测试
    sql = "SELECT SUM(money) FROM wht_Contract"
    a = Sqlserverdb().queryOne(sql)
    print(a[0])
