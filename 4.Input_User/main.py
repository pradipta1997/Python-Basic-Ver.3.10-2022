#INPUT DATA YANG DILAKUKAN OLEH USER DI TERMINAL/INTERPRETED PYTHON

#Secara default input adalah tipe data string
# data = input("Masukan Data: ")

# print("Data yang diinput oleh user ->", data, "Type: ", type(data))


# #Casting Tipe data agar tidak default string.
# angka = int(input("Masukan Data: "))
# angka = float(input("Masukan Data: "))

# print("Data yang diinput oleh user ->", angka, "Type: ", type(angka))


#Bagaimana dengan Boolean ?
data_boolean_biner = bool(int(input("Masukan Data: "))) # <-- harus tricky, data boolean harus dijadikan integer dulu.

print("Data yang diinput oleh user ->", data_boolean_biner, "Type: ", type(data_boolean_biner))