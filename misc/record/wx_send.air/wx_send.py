# -*- encoding=utf8 -*-
__author__ = "zyt"

from airtest.core.api import *

auto_setup(__file__)

wechat_package = "com.tencent.mm"

# clear_app(wechat_package)
# sleep(1.0)
# start_app(wechat_package)

touch(Template(r"tpl1563615295092.png", record_pos=(-0.372, 0.881), resolution=(1080.0, 2340.0)))
touch(Template(r"tpl1563615308656.png", record_pos=(0.276, -0.939), resolution=(1080.0, 2340.0)))
text("旺福", enter=True)
wait(Template(r"tpl1563638053576.png", record_pos=(-0.217, -0.633), resolution=(1080, 2340)),timeout=10)

touch(Template(r"tpl1563637155059.png", record_pos=(-0.227, -0.644), resolution=(1080.0, 2340.0)))

touch(Template(r"tpl1563637179252.png", record_pos=(-0.321, 0.888), resolution=(1080.0, 2340.0)))
text("Hello")
wait(Template(r"tpl1563638148577.png", record_pos=(0.426, 0.244), resolution=(1080, 2340)),timeout=10)


touch(Template(r"tpl1563637293027.png", record_pos=(0.411, 0.834), resolution=(1080.0, 2340.0)))








