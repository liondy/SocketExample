import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5050
BUFFER_SIZE = 1024
# MESSAGE = "Hello, World! "

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data = s.recv(BUFFER_SIZE) #message
print(data.decode())
stat = s.recv(BUFFER_SIZE) #status
num = str(stat, 'utf8')
if int(num)==1:
    MESSAGE = input()
    s.send(MESSAGE.encode('utf-8'))
    data = s.recv(BUFFER_SIZE)
    print(data.decode())
    if int(MESSAGE)==1:
        print("Hai Admin :)")
    if int(MESSAGE)==2:
        print("Silahkan tunggu soal dari admin :)")
else:
    print("Silahkan tunggu soal dari admin :)")