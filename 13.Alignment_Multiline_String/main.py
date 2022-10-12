#WIDTH AND MULTILINE

#Main Data
data_nama         = "Pradipta Ramadhan"
data_usia         = 25
data_tinggi       = 180.1
data_nomor_sepatu = 43

#String Standard
data_string = f"Nama: {data_nama}, Umur: {data_usia}, Tinggi: {data_tinggi}, Ukuran Sepatu: {data_nomor_sepatu}"
print(5*'=' + "Data String Standard" + 5*'=')
print(data_string)

#String Multiline (Dengan menggunakan enter/newline (\n))
data_string = f"Nama: {data_nama}, \nUmur: {data_usia}, \nTinggi: {data_tinggi}, \nUkuran Sepatu: {data_nomor_sepatu}"
print(5*'=' + "String Multiline Newline" + 5*'=')
print(data_string)

#String Multiline (Dengan menggunakan kutip triplets)
data_string = f"""
nama: {data_nama}
Umur: {data_usia}
Tinggi: {data_tinggi}
Ukuran: {data_nomor_sepatu}
"""
print("\n",5*'=' + "String Multiline Kutip Triplets" + 5*'=')
print(data_string)


#Mengatur Width (Membuat menjadi rata kanan (:>5))
data_string = f"""
nama   = {data_nama:>5} 
Umur   = {data_usia:>5}
Tinggi = {data_tinggi:>5}
Ukuran = {data_nomor_sepatu:>5}
"""
print("\n",5*'=' + "Mengatur Width" + 5*'=')
print(data_string)