# UDP Echo Client
# inspired from UDP client code discussed in the class

import socket

server_addr_port = ("127.0.0.1",22223)
bufsize = 1024

soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# creating a new UDP socket object

msgFromClient = input("Enter the msg to be echoed: ")

soc.sendto(msgFromClient.encode(),server_addr_port)
# msg sent to server

msgFromServer = soc.recvfrom(bufsize)
# msg recieved from server

print("Msg recieved from server: {}".format(msgFromServer[0].decode()))
