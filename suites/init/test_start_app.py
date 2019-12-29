#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import time
import pytest

from airtest.core.api import *
from airtest.core.android.android import Android
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from libs.pages.main import *
from libs.utils.path import *

from libs.const.app import *


def test_start_app():
    auto_setup(__file__)

    android_device = connect_device('Android://')
    devs = device()
    print(devs)
    print(devs.list_app(third_only=True))

    # start the app
    start_launch_time = time.time()
    start_app(wechat_package, activity=None)
    snapshot(SNAPSHOTS_PATH+"/wechat.png")
    assert_exists(tab_mine)

    launch_finish_time = time.time()
    print('启动APP所用时间：', launch_finish_time - start_launch_time)

    time.sleep(2)

    # stop the app
    stop_app(wechat_package)



if __name__ == '__main__':
    pass

