#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)

tab_mine = poco("com.tencent.mm:id/bv").offspring("android.widget.LinearLayout").offspring("com.tencent.mm:id/tb")