# 导入测试报告
from HTMLTestRunner import HTMLTestRunner
from public.webClass import *

# 指定当前测试PC端地址
url = "http://test.b1box.net"
f = open(propath() + 'data/config/url.txt', 'w+')
if f.readline() == url:
    pass
else:
    f.write(url)
    f.close()

# 指定测试用例为当前文件夹下的test_case目录
# 通过自定函数获取当前文件所在路径
test_dir = propath() + "date"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='DB*.py')
v_tim = time.strftime("%Y%m%d")
if __name__ == '__main__':
    FileName = propath() + 'report/BDReport/' + v_tim + 'BD_online.htm'
    fp = open(FileName, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='online基础数据添加自动化测试',
                            description='online基础数据添加自动化测试结果统计')
    runner.run(discover)
    fp.close()
