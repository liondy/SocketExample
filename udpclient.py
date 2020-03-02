import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
Message = "Hello World!"

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Message = input("Please enter a string:\n")
clientSock.sendto(Message.encode('utf-8'), (UDP_IP_ADDRESS, UDP_PORT_NO))