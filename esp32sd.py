import os
from machine import Pin, SoftSPI
from sdcard import SDCard

# 接线说明:
# MISO -> GPTO 19
# MOSI -> GPIO 23
# SCK -> GPIO 18
# CS -> GPIO 5

spisd=SoftSPI(-1, miso=Pin(19), mosi=Pin(23), sck=Pin(18))
sd=SDCard(spisd, Pin(5))

print('未挂载SD之前:{}'.format(os.listdir()))

vfs=os.VfsFat(sd)
os.mount(vfs,'/sd')

print('挂载SD开之后:{}'.format(os.listdir()))

os.chdir('sd')

print('SD卡中的文件:{}'.format(os.listdir()))

with open("/sd/test.txt", "w") as f:
    for i in range(1, 101):
        f.write(str(i)+"\n")

print("已经将1 2 3....100写入到SD卡中的text.txt文件")
