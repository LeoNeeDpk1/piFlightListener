import socket, sys
from bindings import bindings
from simcontrol import Simcontrol

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listen_address = ('0.0.0.0', 65000)
sock.bind(listen_address)

if "-test" in sys.argv:
    test = True
else:
    test = False
    s = Simcontrol()

while True:
    try:
        message, address = sock.recvfrom(4096)
    except:
        print('Something went wrong with getting info from pyFlightBox')
    
    try:
        if not test:
            s.event(message)
        else:
            print(bindings[message.decode('utf-8')])
    except Exception as e:
        print('Something went wrong with sending data to simcontrol.py', e)