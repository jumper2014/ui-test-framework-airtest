#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)


class BasePage(object):
    # tab页
    tab_wechat = poco(text="微信")
    tab_contact = poco(text="通讯录")
    tab_discover = poco(text="发现")
    tab_mine = poco(text="我")

    # 切换tab操作
    def switch2main(self):
        self.tab_wechat.click()

    def switch2contact(self):
        self.tab_contact.click()

    def switch2discover(self):
        self.tab_discover.click()

    def switch2mine(self):
        self.tab_mine.click()


if __name__ == '__main__':
    pass