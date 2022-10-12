#LOOPING LIST DAN ENUMERATE

#For Loop List
kumpulan_angka = [4,6,8,3,1,8]

for angka in kumpulan_angka:
    print(f"Kumpulan Angka: {angka}")


peserta = ["Zamrun","Samuel","Samsudin","Mbemba"]

for nama in peserta:
    print(f"Kumpulan nama: {nama}")


#==================================================
print("===========================================")


#For Loop and Range List
kumpulan_angka = [1,2,4,7,3,8,0,9]

lenght = len(kumpulan_angka)

for i in range(lenght):
    print(f"Range angka: {kumpulan_angka[i]}")


#==================================================
print("===========================================")

#While Loop List
print("======================")
kumpulan_angka  = [10,3,5,7,0,5]

lenght = len(kumpulan_angka)
i = 0

while i < lenght:                               # <-- sama saja seperti cara diatas
    print(f"Angka: {kumpulan_angka[i]}")
    i += 1


#==================================================
print("===========================================")


#List Comprehension (using for loop)
data = ["Pradipta",1,2,3,"Ramadhan"]

[print(f"Data: {i}") for i in data]     # <-- cara melakukan looping for dengan cepat pada list


#==================================================
print("===========================================")


#Enumerate
data_list = ["Pradipta",1,2,3,"Ramadhan"]

for index,data in enumerate(data_list):     # <--Enum untuk bisa memberikan value/keys lebih dari satu,
    print(f"index: {index}, Data: {data}")  # juga sekaligus untuk mengetahui nilai "index" dan data value.