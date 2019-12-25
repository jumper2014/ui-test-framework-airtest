#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import time
from airtest.core.api import *
from airtest.core.android.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

if __name__ == '__main__':
    auto_setup(__file__)

    android_device = connect_device('Android://')
    devs = device()
    print(devs)
    print(devs.list_app(third_only=True))

    # start the app
    start_launch_time = time.time()
    start_app('com.tencent.mm', activity=None)

    launch_finish_time = time.time()
    print('启动APP所用时间：', launch_finish_time - start_launch_time)

    time.sleep(2)

    # stop the app
    stop_app('com.tencent.mm')
