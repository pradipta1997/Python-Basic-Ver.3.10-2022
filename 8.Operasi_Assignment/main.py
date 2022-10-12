#ASSIGNMENT OPERATION

'''
Operasi yang dapat dilakukan dengan penyingkatan
Operasi ditambah dengan Assignment.
'''

#sama dengan
a = 5 # <-- Ini adalah assignment
print('Nilai a = ', a)

#tambah sama dengan
a += 1  # <--artinya adalah a = a + 1
print('Nilai a += 1, Nilai menjadi: ', a)

#kurang sama dengan
a -= 2 # <--artinya adalah a = a - 2
print('Nilai a -= 2, Nilai menjadi: ', a)

#kali sama dengan
a *= 5
print('Nilai a *= 5, Nilai menjadi: ', a)

#bagi sama dengan
a /= 2
print('Nilai a /= 2, Nilai menjadi: ', a)

#modulus sama dengan
b = 10
print("\nNilai b =", b)

b %= 3
print("Nilai b %= 3, Nilai b menjadi", b)

#floor division sama dengan
c = 10
print("\nNilai c =", c)

c //= 3
print("Nilai c //= 3, Nilai c menjadi", c)

#eksponen sama dengan..
a = 5
print("\nNilai a =", a)

a **= 3
print("Nilai a **= 3, Nilai a menjadi", a)

#operasi bitwise
#OR
d = True
print("\nNilai d =", d)
d |= False
print("Nilai d |= False, Nilai d menjadi", d)
d = False
d |= False
print("Nilai d |= False, Nilai d menjadi", d)

#AND
d = True
print("\nNilai d =", d)
d &= False
print("Nilai d &= False, Nilai d menjadi", d)
d2 = False
print("\nNilai d2 =", d2)
d2 &= False
print("Nilai d2 &= False, Nilai d menjadi", d2)

#XOR
x = True
print("\nNilai x =", x)
x ^= False
print("Nilai x ^= False, Nilai x menjadi", x)
x2 = False
print("\nNilai x2 =", x2)
x2 ^= False
print("Nilai x2 ^= False, Nilai x menjadi", x2)