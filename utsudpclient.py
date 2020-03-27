import socket

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Message = input("masukan angka:\n")
clientSock.sendto(Message.encode('utf-8'), ("127.0.0.1", 50000))
data, addr = clientSock.recvfrom(1024)
print("Hasil bilangan:", data.decode())