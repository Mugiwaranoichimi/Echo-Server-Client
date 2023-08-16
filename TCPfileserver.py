# TCP based Simple File Server
# os.walk() function learnt from web: https://www.geeksforgeeks.org/os-walk-python/
# socket related code inspired from code discussed in class.

import socket
import os

# searches for given file in the current directory
def found(file_name):
    x = 0
    for root, dirs, files in os.walk("."):
        if file_name in files:
            x = 1
    return x

port = 6000

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# creating a new TCP socket object

soc.bind(('',port))
# binding the server to a port

soc.listen(1)
# listen for incoming connection

while(1):

    (csoc, caddr) = soc.accept()
    msgfromClient = csoc.recvfrom(1024)[0].decode()
    i = msgfromClient.rfind("-")
    file = msgfromClient[:i]
    # file name
    n = int(msgfromClient[i+1:])
    # no.of bytes

    if(found(file)):
        with open(file, "rb") as f:
            f.seek(-(n + 1), 2)
            s = f.read()[-n:]
        csoc.send(s)
    else:
        s = "SORRY!"
        csoc.send(s.encode())

    csoc.close()
