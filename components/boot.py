import network
import esp
import gc

esp.osdebug(None)
gc.collect()

ssid = 'MON_RESEAU_WIFI'
password = 'MON_PASSWORD'

sta_if = network.WLAN(network.STA_IF)

sta_if.active(True)
sta_if.connect(ssid, password)

while not sta_if.isconnected():
    pass

# print('Connection successful')
# print(station.ifconfig())
