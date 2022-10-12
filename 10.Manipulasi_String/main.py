#OPERASI DAN MANIPULASI STRING

# 1. MENYAMBUNG STRING (CONCATENATE)
nama_pertama = "Monkey"
nama_tengah  = "D"
nama_akhir   = "Luffy"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

#===================================================================
print("=======================")

# 2. MENGHITUNG PANJANG STRING
panjang = len(nama_lengkap)
print('Panjang dari ' + nama_lengkap + ' = ' + str(panjang))

#===================================================================
print("=======================")

# 3. OPERATOR UNTUK STRING

d = "D"
status = d in nama_lengkap  # <--Untuk mengecek apakah ada komponen char/string tertentu didalam string
print(d + " ada di " + nama_lengkap + " = " + str(status))

d1 = "d"
status = d1 in nama_lengkap  # <--Untuk mengecek apakah ada komponen char/string tertentu didalam string
print(d1 + " tidak ada di " + nama_lengkap + " = " + str(status))

d1 = "d"
status = d1 not in nama_lengkap  # <--not in, maka hasil nya true
print(d1 + " tidak ada di " + nama_lengkap + " = " + str(status))

#===================================================================
print("=======================")

# 4. MENGULANG STRING
print("wkwkw"*10)
print(20*"wkwk")

#===================================================================
print("=======================")

# 5. INDEXING
print("Index ke-0: " + nama_lengkap[0])
print("Index ke-1: " + nama_lengkap[1])
print("Index ke-2: " + nama_lengkap[2])
print("Index ke-?: " + nama_lengkap[9])
print("Index ke-[-1]: " + nama_lengkap[-1]) # <-- jika minus 1 maka akan mengambil karakter paling belakang
print("Index ke-[-14]: " + nama_lengkap[-14]) # <-- jika minus 14, maka mengambil karakter paling depan
print("Index ke [?] sampai [?]: " + nama_lengkap[0:9]) # <--mengambil jumlah karakter dari sampai ke sampai
print("Index ke [0,2,4,6,8,10]: " + nama_lengkap[0:11:2]) # <-- mengambil dgn increment [2], loncat 2 huruf

#===================================================================
print("=======================")

# 5. MENGAMBIL ITEM PALING KECIL
print("Item paling kecil: " + min(nama_lengkap)) # <-- item yang karakternya paling sedikit di (nama_lengkap)

# 6. MENGAMBIL ITEM PALING BESAR
print("Item paling besar: " + max(nama_lengkap))    # <-- item yang karakternya paling banyak di (nama_lengkap)

#===================================================================
print("=======================")

# 7. MENGETAHUI KODE ASCII PADA KARAKTER
ascii_code = ord(" ")
print("ASCII untuk spasi adalah: " + str(ascii_code))

ascii_code = ord("M")
print("ASCII untuk spasi adalah: " + str(ascii_code)) # <-- untuk mencari key M ASCII nomor berapa (str)

data_ascii = 77
print("Char untuk data ASCII adalah: " + chr(data_ascii)) # <-- untuk mencari ASCII 77 karakter apa (chr)

#===================================================================
print("=======================")

# 8. OPERATOR DALAM BENTUK METHOD
data = "Asep Surasep sepsep"
jumlah = data.count("e")
print("Jumlah karakter yang dihitung adalah: " + str(jumlah))
