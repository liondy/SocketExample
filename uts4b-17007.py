#Ignatius Michael Liondy - 2017730007

import socket
import random

TCP_IP = '127.0.0.1'
TCP_PORT = 60000
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(2)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    angka1 = random.randint(0, 1000)
    angka2 = random.randint(0, 1000)
    angka3 = random.randint(0, 1000)
    res = angka1+angka2+angka3
    message = str(angka1) + ' , ' + str(angka2) + ' , ' + str(angka3)
    conn.send(message.encode())
    input = conn.recv(1024).decode()
    if not input:
        break
    else:
        if(int(input) == res):
            reply = 'benar'
            conn.send(reply.encode())
        else:
            reply = 'salah '
            conn.send(reply.encode())
conn.close()