from public.webClass import *
# 导入测试报告
from HTMLTestRunner import HTMLTestRunner
from public.config import *





# 指定当前测试PC端地址
UrlTest.pc()

# 指定测试用例为当前文件夹下的test_case目录
# 通过自定函数获取当前文件所在路径
test_dir = propath() + "webPc"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='FT0*.py')
if __name__ == '__main__':
    v_tim = time.strftime("%Y%m%d")
    FileName = propath() + 'report/FTRport/' + v_tim + 'FT_online01.htm'
    fp = open(FileName, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='online功能集成自动化测试',
                            description='online自动化测试——主流程功能测试执行结果统计')
    runner.run(discover)
    fp.close()