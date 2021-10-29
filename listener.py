import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listen_address = ('0.0.0.0', 65000)
sock.bind(listen_address)

while True:
    try:
        message, address = sock.recvfrom(4096)
    except:
        print('Somthing went wrong...')
    message = str(message)[2:-1]
    print(message)