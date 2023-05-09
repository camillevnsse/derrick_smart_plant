# code micropython pour l'arrosage de la plante

import urequests as requests
import time
import machine

try:
    import usocket as socket
except Exception:
    import socket


def debug(text):
    url = 'http://192.168.0.25:1234'
    headers = {'Content-Type': 'application/json'}
    data = '{"text": "' + f"{text}" + '"}'
    # r = requests.post(url, data=data, headers=headers)


led = machine.Pin(2, machine.Pin.OUT)
relay = machine.Pin(12, machine.Pin.OUT)  # D6
relay.value(1)

debug('Starting server...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
debug('Server started.')


def water_plant():
    led.value(0)
    relay.value(0)  # on
    time.sleep(3)
    led.value(1)
    relay.value(1)  # off


while True:
    try:
        debug('Start while')
        conn, addr = s.accept()
        conn.settimeout(3.0)
        debug('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        debug('Content = %s' % request)
        water_on = request.find('/water')
        if water_on:
            debug('water_on')
            water_plant()

        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall('<html><body>OK</body></html>')
        conn.close()
        debug('End request')
    except Exception as err:
        data = f"{type(err).__name__} was raised {err}"
        debug(data)
    conn.close()
