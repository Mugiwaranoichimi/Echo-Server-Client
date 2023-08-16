# UDP based Math Server
# inspired from UDP server code discussed in the class

import socket

server_addr_port = ("127.0.0.1",22224)
bufsize = 1024

soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# creating a new UDP socket object

soc.bind(server_addr_port)
# binding the server to a port

print("HI I'M A MATH SERVER :)")

while(1):
    tupl = soc.recvfrom(bufsize)
    msg = tupl[0].decode()
    adr = tupl[1]
    print("Recieved: {}".format(msg))
    x = msg.split()
    ans = 0
    if(x[0] == "add"):
        ans = int(x[1]) + int(x[2])
    if(x[0] == "mul"):
        ans = int(x[1]) * int(x[2])
    if(x[0] == "mod"):
        ans = int(x[1]) % int(x[2])
    if(x[0] == "hyp"):
        ans = int((int(x[1])**2 + int(x[2])**2) ** (1/2))

    soc.sendto(("{}".format(ans)).encode(),adr)
    # send the result to client