#OPERASI KOMPARASI PYTHON

'''
    1.  >  (Lebih besar dari..)
    2.  <  (Lebih kecil dari..)
    3.  >= (Lebih besar sama dengan..)
    4.  <= (Lebih kecil sama dengan..)
    5.  == (Sama dengan..)
    6.  != (Tidak sama dengan..)
    7.  is (Komparasi Identity, jika x adalah y maka true, sebaliknya)
    8.  is not (Komparasi Identity, jika x bukan y maka trus, sebaliknya)
'''

from unittest import result


a = 4
b = 2

#LEBIH BESAR DARI.. (>)
print("====LEBIH BESAR DARI====")
hasil1 = a > 3
print(a, '>', 3, '=', hasil1)
hasil1 = b > 3
print(b, '>', 3, '=', hasil1)
hasil1 = b > 2
print(b, '>', 2, '=', hasil1)

#============================================

#LEBIH KECIL DARI..(<)
print("====LEBIH LECIL DARI====")
hasil1 = a < 3
print(a, '<', 3, '=', hasil1)
hasil1 = b < 3
print(b, '<', 3, '=', hasil1)
hasil1 = b < 2
print(b, '<', 2, '=', hasil1)

#============================================

#LEBIH BESAR SAMA DENGAN..(>=)
print("====LEBIH BESAR SAMA DENGAN====")
hasil1 = a >= 3
print(a, '>=', 3, '=', hasil1)
hasil1 = b >= 3
print(b, '>=', 3, '=', hasil1)
hasil1 = b >= 2
print(b, '>=', 2, '=', hasil1)

#============================================

#LEBIH KECIL SAMA DENGAN..(<=)
print("====LEBIH KECIL SAMA DENGAN====")
hasil1 = a <= 3
print(a, '<=', 3, '=', hasil1)
hasil1 = b <= 3
print(b, '<=', 3, '=', hasil1)
hasil1 = b <= 2
print(b, '<=', 2, '=', hasil1)

#============================================

#SAMA DENGAN..(==)
print("====SAMA DENGAN====")
hasil1 = a == 3
print(a, '==', 3, '=', hasil1)
hasil1 = b == 3
print(b, '==', 3, '=', hasil1)
hasil1 = b == 2
print(b, '==', 2, '=', hasil1)

#============================================

#TIDAK SAMA DENGAN..(==)
print("====TIDAK SAMA DENGAN====")
hasil1 = a != 3
print(a, '!=', 3, '=', hasil1)
hasil1 = b != 3
print(b, '!=', 3, '=', hasil1)
hasil1 = b != 2
print(b, '!=', 2, '=', hasil1)

#============================================

#SEBAGAI KOMPARASI OBJECT IDENTITY (is)
print("====IS, OBJECT IDENTITY====")
x = 5   # <-- ini adalah assignment membuat object
y = 5   # <-- ini adalah assignment membuat object
print('Nilai x =', x, 'ID =', hex(id(x)))   # <-- Untuk cek id memori
print('Nilai y =', y, 'ID =', hex(id(y)))   # <-- Untuk cek id memori
result = x is y
print('x is y =', result)

x = 5   # <-- ini adalah assignment membuat object
y = 6   # <-- ini adalah assignment membuat object
print('Nilai x =', x, 'ID =', hex(id(x)))
print('Nilai y =', y, 'ID =', hex(id(y)))   # <-- Jika value dari variable berbeda maka akan disimpan di memori yg beda
result = x is y # <-- 5 tidak berarti 6, maka false
print('x is y =', result)

#============================================

#SEBAGAI KOMPARASI OBJECT IDENTITY (is not)
print("====IS NOT, OBJECT IDENTITY====")
x = 5   # <-- ini adalah assignment membuat object
y = 5   # <-- ini adalah assignment membuat object
print('Nilai x =', x, 'ID =', hex(id(x)))   # <-- Untuk cek id memori
print('Nilai y =', y, 'ID =', hex(id(y)))   # <-- Untuk cek id memori
result = x is not y
print('x is y =', result)

x = 5   # <-- ini adalah assignment membuat object
y = 6   # <-- ini adalah assignment membuat object
print('Nilai x =', x, 'ID =', hex(id(x)))
print('Nilai y =', y, 'ID =', hex(id(y)))   # <-- Jika value dari variable berbeda maka akan disimpan di memori yg beda
result = x is not y # <-- 5 tidak berarti 6, maka false
print('x is y =', result)