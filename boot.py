# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

import uos, machine

#uos.dupterm(None, 1) # disable REPL on UART(0)

import gc

#import webrepl

#webrepl.start()

gc.collect()


import network

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)

# sta_if.scan()                             # Scan for available access points

sta_if.connect("young-family", "good2best") # Connect to an AP

sta_if.isconnected()                        # Check for successful connection

from main import check_events
import time

time.sleep(4)
check_events()
# # Change name/password of ESP8266's AP:

# ap_if = network.WLAN(network.AP_IF)

# ap_if.config(essid="<AP_NAME>", authmode=network.AUTH_WPA_WPA2_PSK, password="<password>")

