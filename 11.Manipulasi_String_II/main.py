#OPERASI DAN MANIPULASI STRING Part II

#MERUBAH STRING KE UPPER CASE
from tkinter import Variable


var = "Hallo!"
print("Normal Case: " + var)
var = var.upper()
print("Menjadi Upper: " + var)

print("====================")

#MERUBAH STRING KE LOWER CASE
var2 = "HaLlO!"
print("Normal Case: " + var2)
var2 = var2.lower()
print("Menjadi Upper: " + var2)

print("====================")

#PENGECEKAN DENGAN isX METHOD
Variable = "pradipta ramadhan"
apakah_lower = Variable.islower()   # <--Hasilnya Boolean (islower)
print(Variable + "is lower = " + str(apakah_lower))

apakah_upper = Variable.isupper()   # <--Hasilnya Boolean (isupper)
print(Variable + "is upper = " + str(apakah_upper))

print("====================")

#PENGECEKAN DENGAN IS FAMILY

'''
    LIST:
    1. isalpha() <-- Untuk mengecek semua huruf
    2. isalnum() <-- Untuk mengecek huruf & angka
    3. isdecimal() <-- Untuk mengecek angka saja
    4. isspace() <-- Untuk mengecek spasi, tab, newline
    5. istitle() <-- Untuk mengecek semua kata yang dimulai dari huruf besar
'''

Title = "Manipulasi String Dengan Python"
Cek_Title = Title.istitle() # <-- hasil nilainya Boolean
print(Title + " is title = " + str(Cek_Title))

print("====================")

#PENGECEKAN DENGAN STARTSWITH() & ENDSWITH()
cek_starts = "Pradipta Ramadhan".startswith("Pradipta") # <-- Menghasilkan nilai Boolean
print("Start = " + str(cek_starts))

cek_ends = "Pradipta Ramadhan".endswith("Ramadhan") # <-- Menghasilkan nilai Boolean
print("End = " + str(cek_ends))

print("====================")

#PENGGABUNGAN KOMPONEN join() & split()
Array = ['Aku','Sayang','Kamu']

Gabung = ','.join(Array)
print('Data Asli: ', Array)
print('Data Gabung: ', Gabung)

Gabung = ' '.join(Array)
print('Data Asli: ', Array)
print('Data Gabung: ', Gabung)

Gabung = "akuehmsayangehmkamu"
print(Gabung.split('ehm'))

print("====================")

#ALOKASI KARAKTER rjust(), ljust(), center(), strip()
kanan = "Kanan".rjust(10)   #membuat jarak ke kanan
print("'" + kanan + "'")

kiri = "Kiri".ljust(10)     #membuat jarak ke kiri
print("'" + kiri + "'")

tengah = "Tengah".center(20,"-")    #membuat jarak kanan & kiri
print("'" + tengah + "'")

tengah = "Tengah".strip()   #menghilangkan jarak
print("'" + tengah + "'")