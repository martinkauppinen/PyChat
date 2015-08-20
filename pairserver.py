import socket
import threading
import random
import sys
import time

def output(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data: break
        print "Other person: ", data
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
    if msg == "exit":
        conn.send("Server closed")
        break
    conn.send(msg)

thread.join()
print "Connection lost."