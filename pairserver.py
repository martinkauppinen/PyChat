import socket
import threading
import readline
import random
import sys
import time

def output(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data: break
        sys.stdout.write('\r'+' '*(len(readline.get_line_buffer())+2)+'\r')
        print "<Other person>:", data
        sys.stdout.write('> ' + readline.get_line_buffer())
        sys.stdout.flush()
    conn.close()

# Entry point
PORT = int(sys.argv[1])
HOST = ''
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind((HOST, PORT))
mySocket.listen(1)
conn, addr = mySocket.accept()
print 'Horribly insecure connection from:', addr

# Threading stuff
thread = threading.Thread(target=output, args=(conn, addr))
thread.daemon = True
thread.start()

while True:
    msg = raw_input("> ")
    if msg == "\\exit": # Exit command
        try:
            conn.send("Server closed")
        except socket.error:
            print "Funny error message"
        break

    elif msg == "\\help": # Help command
        help = open("help.txt", "r")
        for line in help:
            print line,
        help.close()

    if msg[0] != "\\": conn.send(msg) # If the message starts with a backslash (i.e. it's a command), do not send the message

mySocket.close()
print "Connection lost."
