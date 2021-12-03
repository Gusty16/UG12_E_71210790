print("Test Case 1:")
a = [3,20,100,-35,50]

def nilai_maksimal(db):
    nt = db[0]
    for n in db:
        if n > nt:
            nt = n
    return nt

def nm(db):
    nk = db[0]
    for n in db:
        if n < nk:
            nk = n
    return nk

print(a)
print("Nilai terbesar: ",nilai_maksimal(a))
print("Nilai terkecil: ",nm(a))

print("\nTest Case 2:")
a = [3,20,90,35,75]

def nilai_maksimal(db):
    nt = db[0]
    for n in db:
        if n > nt:
            nt = n
    return nt

def nm(db):
    nk = db[0]
    for n in db:
        if n < nk:
            nk = n
    return nk

print(a)
print("Nilai terbesar: ",nilai_maksimal(a))
print("Nilai terkecil: ",nm(a))
