#function to print number to letter

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

# angka = int(input())
for angka in list(range(1001)):
    print(proses(angka))