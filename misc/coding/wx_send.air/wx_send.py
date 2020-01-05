# -*- encoding=utf8 -*-
__author__ = "zyt"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(force_restart=False)                                                                                                      

poco("com.tencent.mm:id/bv").offspring("com.tencent.mm:id/dcs").offspring("android.widget.LinearLayout").offspring("com.tencent.mm:id/tb").click()

poco("com.tencent.mm:id/bv").offspring("android.widget.LinearLayout").offspring("com.tencent.mm:id/tb").click()







touch(Template(r"tpl1578239937375.png", record_pos=(0.399, 0.107), resolution=(1080, 2340)))

