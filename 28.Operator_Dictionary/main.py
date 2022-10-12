#OPERATOR PADA DICTIONARY

#MAIN DATA
data_dict = {
    'mj':'Meja',
    'kps':'Kipas',
    'ksr':'Kasur',
    'mnt':'Monitor',
    'sjd':'Sajadah',
    'bj':'baju'
}

print(f"Main data dictionary: {data_dict}")


#=============================================
print("======================================")

#MENGECEK PANJANG DICTIONARY (LENDICT)
LENDICT = len(data_dict)
print(f"Panjang data dictionary: {LENDICT}")


#=============================================
print("======================================")

#MENGECEK KEY EXIST ATAU TIDAK (KEY & CHECKKEY)
KEY = "kps"
CHECKKEY = KEY in data_dict # <--Untuk mengecek apakah data key-nya ada/tidak, jika ada (True), jika tidak (False).
print(f"Apakah {KEY} ada didalam data_dict: {CHECKKEY}")


#=============================================
print("======================================")

#MENGAKSES VALUE (read) DENGAN .get()
print(data_dict.get('kps'))
print(data_dict.get('sjd')) # <--Ini akan menampilkan value dari masing-masing key-nya.
print(data_dict.get('mnt'))
print(data_dict.get('ep','data key tidak ada'))  # <--Ini contoh jika key tidak ada dalam main data, maka value akan (none)
                                                 # atau jika di berikan pesan, output yg dikeluarkan bukan none tapi text.

#=============================================
print("======================================")

#MENGUPDATE DATA DICTIONARY
data_dict['bj'] = 'baju-baju'
print(f"Data key sesudah diupdate: {data_dict}")


#=============================================
print("======================================")

#ADD DATA DICTIONARY
data_dict['pk'] = 'Pakaian'
print(f"Data key sesudah ditambah: {data_dict}")


#=============================================
print("======================================")

#UPDATE DATA DENGAN .update() DENGAN CARA LEBIH KEREN

#dengan menggunakan .update(), jika data sudah ada maka yang diupdate data yang sudah ada saja tanpa menambah data lagi
#tapi jika data yang ingin diupdate belum ada, maka akan menambah data baru.
data_dict.update({"ksr":"Kasur Busa"})
print(f"Data yang sudah diupdate dengan .update(): {data_dict}\n")

data_dict.update({"ps":"Playstation"})
print(f"Data yang sudah diupdate dengan .update(): {data_dict}\n")


#=============================================
print("======================================")

#MENGHAPUS DATA DICTIONARY (del)
del data_dict["bj"]
print(f"Data yang dihapus: {data_dict}")