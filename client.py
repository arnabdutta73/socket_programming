import socket  # for sockets
import sys  # for exit

# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

host = 'localhost'
port = 12345

while 1:
    try:
        # receive data from client (data, addr)
        s.bind((host, port))
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print('Server reply : ' + reply.decode())

    except socket.error as msg:
        print('Error Code : ' + str(msg))
        sys.exit()
