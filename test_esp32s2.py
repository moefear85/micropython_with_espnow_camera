from ili9XXX import ili9341
import lvgl as lv
from espidf import HSPI_HOST,VSPI_HOST,SPI_HOST
from time import sleep

display=ili9341(double_buffer=False,miso=7, mosi=4, clk=5, cs=1, dc=3, rst=2, backlight=6, backlight_on=1,spihost=VSPI_HOST, mhz=40, factor=16, hybrid=True)
#lv.init() # display already calls this

scr = lv.obj()
btn = lv.btn(scr)
btn.align_to(lv.scr_act(), lv.ALIGN.CENTER, 0, 0)
label = lv.label(btn)
label.set_text("Hello World!")
lv.scr_load(scr)
