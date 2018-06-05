from PubliCode.webClass import *

# 指定当前测试PC端地址
testurl_pc("http://test.b1box.net")

# 指定测试用例为当前文件夹下的test_case目录
# 通过自定函数获取当前文件所在路径
test_dir = propath() + "FunctionWeb"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='FT0*.py')
if __name__ == '__main__':
    v_tim = time.strftime("%Y%m%d")
    FileName = propath() + 'TestReport/FTRport/' + v_tim + 'FT_online01.htm'
    fp = open(FileName, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='online功能集成自动化测试',
                            description='online自动化测试——主流程功能测试执行结果统计')
    runner.run(discover)
    fp.close()