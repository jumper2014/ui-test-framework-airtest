# -*- encoding=utf8 -*-
__author__ = "zyt"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(force_restart=False)                                                                                                      

poco("com.tencent.mm:id/bv").offspring("com.tencent.mm:id/dcs").offspring("android.widget.LinearLayout").offspring("com.tencent.mm:id/tb").click()

poco("com.tencent.mm:id/bv").offspring("android.widget.LinearLayout").offspring("com.tencent.mm:id/tb").click()






