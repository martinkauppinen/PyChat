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
        print "<Other person>:", data
        sys.stdout.write('> ' + readline.get_line_buffer())
        sys.stdout.flush()

def Main():
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

        elif msg == "\\help": # Help command
            help = open("help.txt", "r")
            for line in help:
                print line,
            help.close()

        if msg[0] != "\\": mySocket.send(msg) # If the message starts with a backslash (i.e. it's a command), do not send the message

    mySocket.close()

if __name__ == "__main__":
    command = ""
    welcome = open("welcome.txt", "r")
    for line in welcome:
        print line,
    welcome.close()
    while command != "\\exit":
        command = raw_input("> ")
        if command == "\\help":
            help = open("help.txt", "r")
            for line in help:
                print line,
            help.close()

        elif command == "\\connect":
            Main()
        
