class A(object):
    bar = 1

    def foo(self):
        print('foo')

    @staticmethod
    def static_foo():
        print('static_foo')
        print(A.bar)

    @classmethod
    def class_foo(cls):
        print('class_foo')
        print(cls.bar)
        cls().foo()


A.static_foo()
A.class_foo()

"""
Python中的self,cls参数
python类里会出现这三个单词，self和cls都可以用别的单词代替，类的方法有三种，

一是通过def定义的 普通的一般的，需要至少传递一个参数，一般用self，这样的方法必须通过一个类的实例去访问，类似于c++中通过对象去访问；

二是在def前面加上@classmethod，这种类方法的一个特点就是可以通过类名去调用，但是也必须传递一个参数，一般用cls表示class，表示可以通过类直接调用；

三是在def前面加上@staticmethod，这种类方法是静态的类方法，类似于c++的静态函数，他的一个特点是参数可以为空，同样支持类名和对象两种调用方式；
"""