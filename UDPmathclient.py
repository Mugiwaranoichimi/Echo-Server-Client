# UDP based Math Client
# inspired from UDP client code discussed in the class

import socket

server_addr_port = ("127.0.0.1",22224)
bufsize = 1024

soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# creating a new UDP socket object

while(1):

    cmd = input("Enter the command: ")

    soc.sendto(cmd.encode(),server_addr_port)
    # send the command to math server

    out = soc.recvfrom(bufsize)
    # result recieved from server

    print("Answer from server: {}".format(int(out[0].decode())))
