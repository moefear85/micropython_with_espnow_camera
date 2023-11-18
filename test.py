from ili9XXX import ili9341
import lvgl as lv
from espidf import HSPI_HOST,VSPI_HOST
from time import sleep

display=ili9341(double_buffer=False,miso=15, mosi=27, clk=26, cs=13, dc=14, rst=12, backlight=25, backlight_on=1,spihost=HSPI_HOST, mhz=40, factor=8, hybrid=True)
#lv.init() # display already inits

scr = lv.obj()
btn = lv.btn(scr)
btn.align_to(lv.scr_act(), lv.ALIGN.CENTER, 0, 0)
label = lv.label(btn)
label.set_text("Hello World!")
lv.scr_load(scr)
sleep(1)