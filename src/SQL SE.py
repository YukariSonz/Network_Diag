#sql server end

import socket
import sqlite3

#TCP connection-- Not finish
def TCPconnection():
    destip=input()
    destpt=7900
    socket1=socket.socket()
    socket1.bind((destip,destpt))
    socket1.listen(1)
    c,addr=socket1.accept()
    

def Receive():
    TCPconnection()
    while True:
        data.recv(1024).decode('ASCII')
        

