senin = ["Algoritma Graf","Sistem Operasi","PAK","Praktikum INLAN"]
sp = [1,3,4,5]
selasa = ["Matematika Teknik","Bhs Indonesia","PKN"]
ss = [2,4,6]
kamis = ["IMK","LogMat","Praktekkom"]
kp = [1,3,4]
jumat = ["Sistem Basis Data","Praktikum Sistem Basis Data","INLAN"]

print("Silahkan Pilih menu (1/2)")
print("1. Tutu")
print("2. Kiko")
p = int(input("Masukkan Pilihan 1/2 :"))

if p == 1:
    h = str(input("Hi Tutu, Silahkan Masukkan hari yang ingin Anda telusuri: "))

    if h == "senin":
        for i in range (len(senin)):
            print("kelas ke-",sp[i],senin[i])
    elif h == "selasa":
        for i in range (len(selasa)):
            print("kelas ke-",ss[i],selasa[i])        
    elif h == "rabu":
        print("Hari rabu Anda tidak ada kelas")
    elif h == "kamis":
        for i in range (len(kamis)):
            print("kelas ke-",kp[i],kamis[i])
    elif h == "jumat":
        for i in range (len(jumat)):
            print("kelas ke-",ss[i],jumat[i])
    elif h == "sabtu":
        print("Hari Sabtu Anda tidak ada kelas")
    elif h == "minggu":
        print("Hari ini Libur")
    else:
        print(h,"Bukan nama hari")
elif p == 2:
    h = str(input("Hi Kiko, Silahkan Masukkan hari yang ingin Anda telusuri: "))

    if h == "senin":
        for i in range (len(senin)):
            print("kelas ke-",sp[i],senin[i])
    elif h == "selasa":
        for i in range (len(selasa)):
            print("kelas ke-",ss[i],selasa[i])        
    elif h == "rabu":
        print("Hari rabu Anda tidak ada kelas")
    elif h == "kamis":
        for i in range (len(kamis)):
            print("kelas ke-",kp[i],kamis[i])
    elif h == "jumat":
        for i in range (len(jumat)):
            print("kelas ke-",ss[i],jumat[i])
    elif h == "sabtu":
        print("Hari Sabtu Anda tidak ada kelas")
    elif h == "minggu":
        print("Hari ini Libur")
    else:
        print(h,"Bukan nama hari")
