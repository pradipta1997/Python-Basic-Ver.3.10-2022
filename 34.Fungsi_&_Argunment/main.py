#FUNCTION AND ARGUMENT(input)

# TEMPLATE
# def nama_fungsi(argument):
#     Badan fungsi

#INPUT NAMA
def function(name):
    '''Fungsi (function) akan menerima input dari argument (name)'''
    print(f"Hallo, my name is {name}")

function("Pradipta Ramadhan")   # <--Mengisi nilai argument

#===========================================================================

#INPUT PROGRAM TAMBAH
def tambah(angka1,angka2):
    '''Fungsi Tambah'''
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(5,10)
tambah(1000,1)

#===========================================================================

#INPUT STRING
def say_hi(list_peserta):
    '''Fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

nama = ["Anonymous 1", "Anonymous 2", "Anonymous 3"]

say_hi(nama)