#FOR LOOPING (PERULANGAN)

#INI DIBUAT DENGAN METODE LIST
angka_list = [0,1,2,3,4,5]
print(angka_list)

for i in angka_list:
    print(f"i sekarang --> {i}")

print("Baris akhir program..")


#====================================
print("========================")

#INI DIBUAT DENGAN METODE RANGE
angka_range = range(5)  # <--Yang akan dicetak 0,1,2,3,4 saja, 5 sebagai angka terakhir batas tidak dicetak.
print(angka_range)  # <--Jika dicetak langsung seperti ini maka akan menampilkan ouput (0,5) saja.

for i in angka_range:
    print(f"i sekarang --> {i}")

print("Baris akhir program..")


#====================================
print("========================")

#INI DIBUAT DENGAN METODE RANGE(ex:1,9)
angka_range = range(1,9)  # <--Menentukan angka awal & akhir, angka/value akhir yg diinput tidak akan tercetak.

for i in angka_range:
    print(f"i sekarang --> {i}")

print("Baris akhir program..")


#====================================
print("========================")

#INI DIBUAT DENGAN METODE STRING
data_string = "Pradipta Ramadhan"   # <-- Output ini akan melooping huruf perhuruf secara berurutan.

for i in data_string:
    print(i)

print("Baris akhir program..")