#CONTOH GENERIC

#STRING
from this import d


nama = "Dipta"
format_str = "Nama saya adalah " + nama # <-- ini adalah format string menggunakan cara lama
print(format_str)

nama = "Dipta"
format_str = f"Hallo, nama saya adalah {nama}" # <-- ini adalah format string menggunakan cara baru
print(format_str)

#=============================================
print("=======================================")

#BOOLEAN
boolean = True
format_str = f"Boolean = {boolean}"
print(format_str)

#=============================================
print("=======================================")

#NUMBER
angka = 2005.5
format_str = f"Nomor saya adalah {angka}"   # <-- f adalah format
print(format_str)

angka = 10
format_str = f"Bilangan bulat: {angka:d}"   # <-- Bilangan Bulat | :d itu untuk membulatkan suatu bilangan
print(format_str)

angka = 2000000
format_str = f"Bilangan dengan ordo ribuan: {angka:,}" # <-- Bilangan Ribuan | :, itu untuk memisahkan angka yg banyak
print(format_str)

angka = 2005.54321
format_str = f"Bilangan Desimal: {angka:.2f}"   # <-- Bilangan Desimal | :.2f untuk menampilkan berapa angka stlh (,)
print(format_str)

angka = 2005.54321
format_str = f"Bilangan Desimal: {angka:010.3f}"   # <-- Menampilkan Leading Zero | :010.3f untuk menambah 0 di awal
print(format_str)


angka_plus = +10
angka_minus = -10
format_plus = f"Ini format plus: {angka_plus:+}"    # <--Menampilkan tanda (+) dengan :+
format_minus = f"Ini format minus: {angka_minus:+}" # <--Menampilkan tanda (-)  

print(format_plus)
print(format_minus)


persentase = 0.045
format_persen = f"Nilai Persen: {persentase:.2%}"   # <--Menampilkan persen dengan :%
print(format_persen)


harga_ayam = 50000
jumlah_ayam = 5
format_str = f"Total harga ayam adalah: Rp.{harga_ayam*jumlah_ayam:,}" #<--Operasi Aritmatika didalam placeholder
print(format_str)


number = 255    #Format Menampilkan angka lain (Binary, Octal, Hexadecimal)
format_binary = f"Format Binary: {bin(number)}"
format_octal  = f"Format Octal: {oct(number)}"
format_hex    = f"Format Hexadecimal: {hex(number)}"
print(format_binary)
print(format_octal)
print(format_hex)
