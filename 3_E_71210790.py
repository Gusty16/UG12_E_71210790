angka = int(input("Masukkan Angka: "))
for g in range(angka):
    print(" "*(angka-g-1)+'* '*(g+1))
for g in range(angka-1):
        print(' '*(g + 1) + "* "*(angka - g - 1))
