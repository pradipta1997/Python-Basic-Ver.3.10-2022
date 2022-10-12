#LIST BIASA ATAU ARRAY ITU MENGAKSES DENGAN MENGGUNAKAN INDEXING [0],[1],[2],[3]
data_list = ["Laptop","Handphone","Charger","Tas","Vape"]
print(f"Data list: {data_list}")
print(f"Mengambil data list berdasarkan indexing: {data_list[0]}")
print(f"Mengambil data list berdasarkan indexing: {data_list[4]}")

#=================================================================
print("==========================================================\n")

#DICTIONARY (ASSOCIATIVE ARRAY), MENGAKSES MENGGUNAKAN KEYS BUKAN INDEX SEPERTI PADA LIST
#(INDENTIFIER -> KEY)

data_dict = {
    # 'key':'value',    <--Contoh rumus penulisan dictionary
    'ltp':'Laptop',
    'hp' : 'Handphone',
    'chr' : 'Charger',
    'ts' : 'Tas',
    'vp' : 'Vape',
    'nmbr' : 100
}

print(f"Main data dictionary berdasarkan key: {data_dict}")
print(f"Data dict yang diambil: {data_dict['chr']}")
print(f"Data dict yang diambil: {data_dict['ltp']}")