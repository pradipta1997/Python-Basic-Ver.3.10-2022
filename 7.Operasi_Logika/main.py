#OPERASI LOGIKA ATAU BOOLEAN

'''
    1. not
    2. or
    3. and
    4. xor
'''

#NOT
print("======NOT======")
a = False
c = not a   # <-- var c bukan a
print('data a =', a)
print('----------NOT')
print('data c =', c)

#==============================================================

#OR (Jika salah satu true, maka hasilnya true)
print("======OR======")
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = True
c = a or b
print(a, 'OR', b, ' =', c)

a = True
b = False
c = a or b
print(a, ' OR', b, '=', c)

a = True
b = True
c = a or b
print(a, ' OR', b, ' =', c)


#==============================================================

#AND (Jika salah satu False, maka hasilnya False)
print("======AND======")
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)

a = False
b = True
c = a and b
print(a, 'AND', b, ' =', c)

a = True
b = False
c = a and b
print(a, ' AND', b, '=', c)

a = True
b = True
c = a and b
print(a, ' AND', b, ' =', c)


#==============================================================

#XOR (Akan True jika salah satu true, sisanya false)
print("======XOR======")
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)

a = True
b = False
c = a ^ b
print(a, ' XOR', b, '=', c)

a = True
b = True
c = a ^ b
print(a, ' XOR', b, ' =', c)
