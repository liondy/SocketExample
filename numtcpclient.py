import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
number = input("Masukkan angka 1-1000:\n")
s.send(bytes(str(number), 'utf8'))
data = s.recv(BUFFER_SIZE)
s.close()

print("Terbilang: ", data.decode())
