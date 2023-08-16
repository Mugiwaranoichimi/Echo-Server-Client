# UDP Echo Server
# inspired from UDP server code discussed in the class

import socket

server_addr_port = ("127.0.0.1",22223)
bufsize = 1024

soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# creating a new UDP socket object

soc.bind(server_addr_port)
# binding the server to a port

print("HI I'M AN ECHO SERVER :)")

while(1):
    tupl = soc.recvfrom(bufsize)
    msg = tupl[0]
    # msg recieved from client

    adr = tupl[1]
    # client ip address

    print("Msg recieved from client: {}".format(msg.decode()))

    soc.sendto(msg,adr)
    # msg sent back to client