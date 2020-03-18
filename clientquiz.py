import socket
import threading
import time

tEv = threading.Event()
tShutdown = threading.Event()

def receving(name, sock):
    shutdown = False
    while not shutdown:
        try:
            data = sock.recvfrom(1024)
            print(str(data))
            if '?' in data:
                tEv.set()
            if data == "The game is finished":  # message from server to stop
                tShutdown.set()
                shutdown = True
        except:
            pass
        finally:
            pass

#host = '192.168.26.86'
host = '127.0.0.1'
port = 4042 #pick any free port currently on the computer

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Start listener
rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

# Join the game
alias = input("Name: ")
s.send(alias.encode('utf-8'))

while 1:
    if tEv.wait(1.0):
        tEv.clear()
        message = input(alias + ", what is your answer ?  -> ")
        if message != '':
            s.send(alias + ": " + message.encode('utf-8'))
    if tShutdown.is_set():
        running = False

rT.join()
s.close()