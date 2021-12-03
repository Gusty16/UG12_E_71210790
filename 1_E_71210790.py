ad = int(input("Masukkan awal deret: "))
akd = int(input("Masukkan akhir deret: "))

if ad % 2 == 0:
    for i in range (ad,akd,2):
        if (i % 5 == 0):
            continue
            print(i,end=" ")
        elif (i % 9 == 0):
            continue
        print(i,end=" ")
else:
    adt = ad+1
    for i in range (adt,akd,2):
        if (i % 5 == 0):
            continue
            print(i,end=" ")
        elif (i % 9 == 0):
            continue
        print(i,end=" ")
