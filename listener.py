import socket, sys
from bindings import bindings
from simcontrol import Simcontrol

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listen_address = ('0.0.0.0', 65000)
sock.bind(listen_address)

if "--test" in sys.argv:
    test = True
else:
    test = False
    s = Simcontrol()

def quit():
    print("\nClosing " + str(listen_address) + "...")
    sock.close()
    if not test:
        print("Closing SimConnect connection...")
        s.quit_connect()
    print("Exiting listener...")
    exit(1)

while True:
    try:
        message, address = sock.recvfrom(4096)
    except KeyboardInterrupt:
        quit()
    except:
        print('Something went wrong with getting info from pyFlightBox')
    
    
    message = message.decode('utf-8')
    try:
        if not test:
            s.input_distributor(message)
        else:
            try:
                print(bindings[message])
            except:
                print("NOT IN BINDNINGS: " + message)
    except KeyboardInterrupt:
        quit()
    except Exception as e:
        print('Something went wrong with sending data to simcontrol.py', e)