#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


from libs.pages.base import *


class WechatPage(BasePage):
    # 按钮
    btn_search = poco("com.tencent.mm:id/r_")
    btn_add = poco("com.tencent.mm:id/rb")


