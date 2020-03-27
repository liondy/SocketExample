import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 60000))

data = s.recv(1024)
data = data.decode()
bilangan = data.split()
total = int(bilangan[0]) + int(bilangan[1]) + int(bilangan[2])
s.send(str(total).encode('utf-8'))

data = s.recv(1024)
data = data.decode()
print(data)
s.close()