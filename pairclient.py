import socket
import threading
import readline
import random
import sys
import time

help = open("help.txt", "r")

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
    if msg == "\\exit": # Exit command
        try:
            mySocket.send("User disconnected")
        except socket.error:
            print "Funny error message"
        break

    elif msg == "\help": # Help command
        for line in help:
            print line,

    if msg[0] != "\\": mySocket.send(msg) # If the message starts with a backslash (i.e. it's a command), do not send the message

mySocket.close()
help.close()
