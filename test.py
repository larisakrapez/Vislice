def je_prastevilo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    kandidat_za_delitelje = 3
    while kandidat_za_delitelje ** 2 <= n:
        if n % kandidat_za_delitelje == 0:
            return False
        else:
            kandidat_za_delitelje += 2
    return True

for i in range(200):
    if je_prastevilo(i):
        print(i)