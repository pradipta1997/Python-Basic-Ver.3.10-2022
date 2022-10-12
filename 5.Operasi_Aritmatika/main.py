#OPERASI ARITMATIKA MENGGUNAKAN PYTHON

#Assingment
from re import X
from time import process_time_ns


a = 10
b = 5

#Operasi Tambah (+)
Tambah = a + b
print(a, '+', b, '=', Tambah)

#Operasi Pengurangan (-)
Kurang = a - b
print(a, '-', b, '=', Kurang)

#Operasi Perkalian (x)
Kali = a * b
print(a, 'x', b, '=', Kali)

#Operasi Pembagian (/)
Bagi = a / b
print(a, '/', b, '=', Bagi) # <-- Pada Python ouput dari pembagian otomatis tipe data float.

#Operasi Eksponen/Pangkat (^)
Pangkat = a ** b
print(a, '^', b, '=', Pangkat)

#Operasi Modulus/Sisa Pembagian (%)
Modulus = a % b
print(a, '%', b, '=', Modulus)

#Operasi Floor Division/Kebalikan dari Modulus (//)
FD = a // b
print(a, '//', b, '=', FD)

#=============================================================
print("===============")

#Operasi Prioritas Operasi (Operational Precedence)
"""
YANG DILAKUKAN PERTAMA KALI DARI PERHITUNGAN SESUAI URUTANNYA:
    1.  () <--Yaitu yang berada didalam tanda kurung.
    2.  Exponen **
    3.  Perkalian dan teman-temannya * / ** % //
    4.  Pertambahan dan Pengurangan + -
"""

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // X
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=', hasil)

hasil2 = x ** y * (z + x) / y - y % z // X      # <-- Maka yang dikerjakan pertama adalah yang berada didalam kurung
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=', hasil2)

hasil3 = x + y * z
print(x, '+', y, '*', z, '=', hasil3)

hasil4 = (x + y) * z
print(x, '+', y, '*', z, '=', hasil4)
