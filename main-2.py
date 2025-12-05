# Neues main.py von GitHub
# 05-DEC-2025
#
import ugit
from machine import Pin
import utime

pin = Pin(0,Pin.IN,Pin.PULL_UP)
if pin.value() is 0:
    ugit.pull_all()
    pass
    
#main code here
TIME_MS=100
LED = Pin("LED", Pin.OUT)
while True:
    LED.on()
    utime.sleep_ms(TIME_MS)
    LED.off()
    time.sleep_ms(TIME_MS)