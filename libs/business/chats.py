#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


from libs.pages.page import *
from airtest.core.api import *


def send_msg_to(name, msg):
    chats_page.click_name(name)
    dialog_page.text_input.click()
    text(msg)
    dialog_page.btn_send.click()
    dialog_page.btn_back.click()


if __name__ == '__main__':
    pass