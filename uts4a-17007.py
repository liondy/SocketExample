import socket
def hitung(angka):
    if(angka%2==0):
        res = 'genap'
    else:
        res = 'ganjil'
    return res


UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 50000
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

while True:
    data, addr = serverSock.recvfrom(1024)
    print("Connection From: ", addr)
    num = str(data, 'utf8')
    hasil = hitung(int(num))
    serverSock.sendto(hasil.encode('utf8'),(UDP_IP_ADDRESS, UDP_PORT_NO))