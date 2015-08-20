import socket
import threading
import readline
import random
import sys
import time

def output(mySocket):
    while True:
        data = mySocket.recv(1024)
        if not data: break
        sys.stdout.write('\r'+' '*(len(readline.get_line_buffer())+2)+'\r')
        print "Other person:", repr(data)
        sys.stdout.write('> ' + readline.get_line_buffer())
        sys.stdout.flush()

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
        try:
            mySocket.send("User disconnected")
        except socket.error:
            print "Funny error message"
        break
    mySocket.send(msg)
mySocket.close()