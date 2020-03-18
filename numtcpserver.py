#Ignatius Michael Liondy - 2017730007

import socket

satuan = ['','satu','dua','tiga','empat','lima','enam','tujuh','delapan','sembilan','sepuluh','sebelas','dua belas','tiga belas','empat belas','lima belas','enam belas','tujuh belas','delapan belas','sembilan belas']
def proses(angka):
    res = ''
    ratusan = angka // 100
    sisa = angka % 100
    puluhan = sisa // 10
    stuan = angka % 10
    if(ratusan==1):
        res = 'seratus '
    elif(ratusan>1 and ratusan<10):
        res += satuan[ratusan] + ' ratus '
    elif(ratusan==10):
        res = 'seribu'
    if(sisa>=20):
        res += satuan[puluhan] + ' puluh '
        res += satuan[stuan]
    elif(sisa < 20):
        res += satuan[sisa]
    return res


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    num = str(data, 'utf8')
    print('Angka terkirim: '+num)
    hasil = proses(int(num))
    conn.send(str(hasil).encode('utf8'))  # echo
conn.close()