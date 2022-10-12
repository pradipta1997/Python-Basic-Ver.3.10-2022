#MEMBUAT MACAM-MACAM LIST

#LIST KUMPULAN DATA NUMBERS
numbers = [1,2,3,4,5,6]
print(f"List kumpulan data numbers: {numbers}")


#=============================================================
print("======================================================")


#LIST KUMPULAN DATA STRING
data_string = ["a","b","c","d","e","f"]
print(f"List kumpulan data string: {data_string}")


#=============================================================
print("======================================================")


#LIST KUMPULAN DATA BOOLEAN
data_boolean = [True,False,True,True]
print(f"List kumpulan data boolean: {data_boolean}")


#=============================================================
print("======================================================")


#LIST KUMPULAN DATA CAMPURAN
data_campuran = [1,"Pradipta",2,"Ramadhan"]
print(f"List kumpulan data campuran: {data_campuran}")


#=============================================================
print("======================================================")


#CARA ALTERNATIF MEMBUAT LIST (ADVANCE)
data_range = range(1,10,2) # <--range(start,stop,jump step/increment)
# print(data_range)
data_list = list(data_range)
print(f"List Range: {data_list}")


#=============================================================
print("======================================================")


#MEMBUAT LIST DENGAN FOR LOOP/LIST COMPREHENSION (ADVANCE)
list_pakai_for = [i**2 for i in range(1,10)]
print(f"List dengan For Loop: {list_pakai_for}")


#=============================================================
print("======================================================")


#MEMBUAT LIST DENGAN FOR & IF (ADVANCE)
list_pakai_for_if = [i for i in range(0,10) if i != 5] # <--Sampai angka 5 akan di skip
print(f"List dengan For Loop & IF: {list_pakai_for_if}")

list_pakai_for_if = [i for i in range(0,10) if i%2 == 0] # <--Step per 2 angka
print(f"List dengan For Loop & IF: {list_pakai_for_if}")

list_pakai_for_if = [i for i in range(0,10) if i%2 != 0] # <--Step per 2 angka | dan angka 0 di skip
print(f"List dengan For Loop & IF: {list_pakai_for_if}")