#CASTING TIPE DATA
#ADALAH UNTUK MERUBAH DARI SATU TIPE DATA KE TIPE LAIN
#TIPE DATA = (int, float, str, boolean)

#INTEGER
print("====INTEGER====")

data_int = 9;
print("Data = ", data_int, "Type = ", type(data_int))

data_float = float(data_int)    #<-- variable model indirect (variable didalam variable)
data_str = str(data_int)
data_bool = bool(data_int)
print("Data = ", data_float, "Type = ", type(data_float))
print("Data = ", data_str, "Type = ", type(data_str))
print("Data = ", data_bool, "Type = ", type(data_bool))

#==========================================================================================

#FLOAT
print("====FLOAT====")

data_float = 9.5;
print("Data = ", data_float, "Type = ", type(data_float))

data_int = int(data_float)    #<-- didalam float ke integer value akan dibulatkan ke bawah (float 9.9 -> int 9)
data_str = str(data_float)
data_bool = bool(data_float)
print("Data = ", data_int, "Type = ", type(data_int))
print("Data = ", data_str, "Type = ", type(data_str))
print("Data = ", data_bool, "Type = ", type(data_bool))


#==========================================================================================

#BOOLEAN
print("====BOOLEAN====")

data_boolean = True;
print("Data = ", data_boolean, "Type = ", type(data_boolean))

data_int = int(data_boolean)
data_str = str(data_boolean)
data_float = float(data_boolean)
print("Data = ", data_int, "Type = ", type(data_int))
print("Data = ", data_str, "Type = ", type(data_str))
print("Data = ", data_float, "Type = ", type(data_float))


#==========================================================================================

#STRING
print("====STRING====")

data_str = "";
print("Data = ", data_str, "Type = ", type(data_str))

data_int = int(data_str)    #<--String harus angka
data_float = float(data_str) #<--String harus angka
data_bool = bool(data_str)  #<--False jika String kosong
print("Data = ", data_int, "Type = ", type(data_int))
print("Data = ", data_float, "Type = ", type(data_float))
print("Data = ", data_bool, "Type = ", type(data_bool))