# TCP based Simple File client
# socket related code inspired from code discussed in class

import socket

serverName = 'localhost'
serverPort = 6000

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# creating a new TCP socket object

soc.connect((serverName,serverPort))
# connect to the server

file = input("Input the filename: ")
n = input("Enter the no.of bytes: ")
soc.send((file + "-" + n).encode())
# sent filename and n to server

servermsg = soc.recv(1024)
# msg from server

if(servermsg.decode() == "SORRY!"):
    print("Server says that the file does not exist.")
else:
    newfile = file + '1'
    fnew = open(newfile,"w")
    fnew.write(servermsg.decode())
    # writing n bytes to new file
    fnew.close()

soc.close()