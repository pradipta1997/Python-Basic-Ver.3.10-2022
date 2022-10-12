#MAIN DATA
data_angka = [1,1,6,8,9,3,5,7,8,5,3,8,9,4,1,3,7,7,9,0,4,5,8,0,3,6,3,4,7,9,2,1]
print("Main Data List: ", data_angka)

#MENCARI DATA YANG DIINGINKAN
jumlah_angka1 = data_angka.count(1)
print("Jumlah angka 1 pada list: ", jumlah_angka1)
jumlah_angka0 = data_angka.count(0)
print("Jumlah angka 0 pada list: ", jumlah_angka0)
jumlah_angka9 = data_angka.count(9)
print("Jumlah angka 9 pada list: ", jumlah_angka9)

#=====================================================
print("===============================================")

#MENGAMBIL POSISI DATA (index)
data_string = ["Apel","Kelapa","Rambutan","Jeruk","Manggis","Nanas","Pepaya","Sirsak"]
print("Main Data: ", data_string)

index_Apel = data_string.index("Apel") # <--Untuk mencari no index ke berapa value tersebut
print("Index Apel: ", index_Apel)
index_Pepaya = data_string.index("Pepaya")
print("Index Pepaya: ", index_Pepaya)

#=====================================================
print("===============================================")

#MENGURUTKAN POSISI DATA LIST (sort)
print(f"Data angka lama sebelum diurutkan: {data_angka}")

data_angka.sort()   # <--Untuk mengurutkan data list 1-sekian
print(f"Data angka baru setelah diurutkan: {data_angka}\n")


print(f"Data buah lama sebelum diurutkan: {data_string}")

data_string.sort()
print(f"Data buah baru setelah diurutkan: {data_string}")

#=====================================================
print("===============================================")

#MENGURUTKAN POSISI DATA LIST DIBALIK (reverse)
data_angka.sort()
print("Data angka disortir 1-10", data_angka)
data_angka.reverse()
print(f"Data angka direverse 10-1 {data_angka}\n")

data_string.sort()
print(f"Data buah disortir a-z {data_string}")
data_string.reverse()
print(f"Data buah direverse z-a {data_string}")