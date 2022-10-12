#COPY DAN POP PADA DICTIONARY

#MAIN DATA
teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}

#PENG-COPY-AN DATA DARI SATU VARIABLE KE VARIABLE LAINNYA
friends = teman_teman.copy()    # <--Meng-copy data yang ada di variable (teman-teman)
print(f"Variable teman_teman: {teman_teman}\n") # <--Hasil output yang sama
print(f"Variable friends: {friends}")   # <--Hasil output yang sama
print(hex(id(teman_teman))) # <--cek id
print(hex(id(friends))) # <--cek id


print("===============================================================================")

#HASIL OUTPUT SUDAH BERBEDA SETELAH PERUBAHAN
teman_teman["cuy"] = "ucur surucuken"
print(f"Variable teman_teman: {teman_teman}\n") # <--Hasil output sudah berbeda setelah perubahan
print(f"Variable friends: {friends}")   # <--Hasil output sudah berbeda setelah perubahan


print("===============================================================================")

#POP DICTIONARY (DIAMBIL BERDASARKAN KEY)
dataAsep = friends.pop("sep")   # <--data Asep sudah di transfer ke variable (dataAsep) 
print(f"Data Asep = {dataAsep}")
print(f"Friends = {friends}")   # <--data Asep akan hilang di list variable (friends)


print("===============================================================================")

#POP ITEM DICTIONARY (YANG DIAMBIL DATA YANG TERAKHIR SAJA)
dataTerakhir = friends.popitem()    # <--Untuk mengambil data terakhir saja
print(f"Data terakhir: {dataTerakhir}")
print(f"Friends: {friends}")