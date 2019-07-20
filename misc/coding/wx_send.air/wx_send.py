# -*- encoding=utf8 -*-
__author__ = "zyt"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(force_restart=False)

wx_tab = poco("com.tencent.mm:id/bp").offspring("android.widget.LinearLayout").offspring("com.tencent.mm:id/d7b")

search_btn = poco("android.widget.LinearLayout").offspring("com.tencent.mm:id/jd")
search_input = poco("android.widget.LinearLayout").offspring("com.tencent.mm:id/c1").child("android.widget.RelativeLayout").offspring("com.tencent.mm:id/kh")


if wx_tab:       
    wx_tab.click()
    sleep(1)
if search_btn:
    search_btn.click()
    sleep(1)
if search_input:
    search_input.click()
    sleep(1)
    text("旺福", enter=True)
   


