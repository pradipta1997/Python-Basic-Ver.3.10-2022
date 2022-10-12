#NESTED LIST (LIST BERSARANG)
print("\n")

#LIST BIASA
data_list_biasa = [1,2,3,4]
print(f"List biasa = {data_list_biasa}")

#=========================================
print("===================================")

#LIST 2D
data_0 = [1,2]
data_1 = [3,4,5]

list_2D = [data_0, data_1]
print(f"List 2D = {list_2D}")
print("\n")

#=========================================
print("===================================")

#CONTOH PENGGUNAAN LIST BERSARANG (NESTED LIST)
mobil_1 = ["Toyota","Avanza","Automatic",1300]
mobil_2 = ["Mitsubishi","Pajero","Manual",2442]
mobil_3 = ["Toyota","Alphard","Manual",3456]
mobil_4 = ["Toyota","Fortuner","Manual",2755]
mobil_5 = ["Nissan","Teana","Manual",2488]
mobil_6 = ["Honda","Civic","Automatic",1498]

list_mobil = [mobil_1,mobil_2,mobil_3,mobil_4,mobil_5,mobil_6]
print(f"List mobil: {list_mobil}")
print("\n")

#=========================================
print("===================================")

#CONTOH PENGGUNAAN LIST BERSARANG DENGAN LOOPING (NESTED LIST | FOR LOOP)
for mobils in list_mobil:
    print(f"Merk\t\t: {mobils[0]}")
    print(f"Nama\t\t: {mobils[1]}")
    print(f"Transmisi\t: {mobils[2]}")
    print(f"CC\t\t: {mobils[3]}\n")