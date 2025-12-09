# Altes main.py
# 11-OKT-2025
#
import ugit
from machine import Pin, reset
from init import wlanconnect
import time

pin = Pin(0,Pin.IN,Pin.PULL_UP)
LED = Pin("LED", Pin.OUT)

   
# Hauptprogramm 
wlanstat = wlanconnect()

if (pin.value() == 0) and (wlanstat == 3):
# Falls GPIO0 auf Masse liegt und eine WiFi-Verbindung aktiv ist
    print("Updating ....")
    ugit.pull_all()
    print("Update done !")
    time.sleep_ms(2000)
    machine.reset()

######################################################
# Dieser Programmcode wird nur ausgeführt, wenn GPIO auf High liegt
# oder keine WiFi Verbundung existiert
TIME_MS=1000
for i in range(6):
    LED.on()
    time.sleep_ms(TIME_MS)
    LED.off()
    time.sleep_ms(TIME_MS)

print("Programmende")
