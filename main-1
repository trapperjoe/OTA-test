# main-1.py
# Kopieren einer ASCII Datei von GitHub
#
# 02-DEC-2025
#
import ugit
from machine import Pin, reset
from init import wlanconnect

# Hauptprogramm 
wlanstat = wlanconnect()

# Bestimme Dateinamen
# Local Datei:
l_file = "DfR.txt" # Name der Datei auf dem Raspi

# Remote Datei:
github_path = "https://raw.githubusercontent.com/"
github_dir = "trapperjoe/OTA-test/master/"
# github_dir = "<user>+</repository>+</master>
r_file = "DfR.txt" # Name der Datei auf GitHub
r_link = github_path + github_dir + r_file
 
# Lade die Datei DfR.txt von GitHub
ugit.pull(l_file, r_link)
print("Update done !")
#
print()
print("*************************************")
print("Eine neue Datei mit dem Namen: ")
print("'DfR.txt' sollte jetzt vorhanden sein")
print("*************************************")



