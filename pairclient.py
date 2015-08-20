import socket
import threading
import random
import sys
import time

def output(mySocket):
    while True:
        data = mySocket.recv(1024)
        if not data: break
        print "Other person:", repr(data)

HOST = raw_input("Enter host: ")
if HOST == "": HOST = "localhost"

PORT = int(raw_input("Enter port: "))
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((HOST, PORT))

# Threading stuff
thread = threading.Thread(target=output, args=(mySocket,))
thread.daemon = True
thread.start()

while True:
    msg = raw_input("> ")
    if msg == "exit":
        mySocket.send("User disconnected")
        break
    mySocket.send(msg)
thread.join()
mySocket.close()