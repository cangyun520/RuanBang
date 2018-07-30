# encoding:utf-8
"""
 * Created by Arvin.liu on 2018-7-28.
 * QQ 405367236
"""
import uiautomator2 as u2
from time import sleep

d = u2.connect('127.0.0.1:6555')
# 启动App
d.app_start("com.alibaba.android.rimet")


sleep(2)

# 停止app
d.app_stop("com.alibaba.android.rimet")