import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5050
BUFFER_SIZE = 20
konek = 0
status = 1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
while 1:
    conn, addr = s.accept()
    print('Connection address:', addr)
    konek+=1
    MESSAGE = "Halo, Selamat Datang di Server Quiz! "
    if status==1 :
        MESSAGE += "Silahkan Pilih Role Anda (tulis angkanya saja):\n1:Admin\n2:Peserta"
    else : 
        MESSAGE += "Kamu adalah Peserta ke-{konek}".format(konek=konek)
    conn.send(MESSAGE.encode())
    conn.send(bytes(str(status), 'utf8'))
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("received data:", data.decode())
    if int(data.decode()) == 1 :
        status = 0
        konek-=1
        MESSAGE = "OKE! Kamu adalah admin dari quiz ini!"
    else:
        MESSAGE = "Kamu adalah Peserta ke-{konek}".format(konek=konek)
    conn.send(MESSAGE.encode())
