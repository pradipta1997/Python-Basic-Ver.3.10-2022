#MULTI KEYS & NESTING DICTIONARY

import datetime # <--Import Package

#MAIN DATA & MULTIKEYS
mahasiswa1 = {
    'nama':'Pradipta',
    'nim':'123456789',
    'sks_lulus':140,
    'beasiswa':False,
    'lahir':datetime.datetime(1997,1,30)
}

mahasiswa2 = {
    'nama':'Mbemba',
    'nim':'1234512345',
    'sks_lulus':130,
    'beasiswa':True,
    'lahir':datetime.datetime(1998,4,12)
}

mahasiswa3 = {
    'nama':'Mpudi',
    'nim':'1234092634',
    'sks_lulus':120,
    'beasiswa':False,
    'lahir':datetime.datetime(1999,2,19)
}

#=============================================

#NESTING DICTIONARY
data_mahasiswa = {
    'MAH001':mahasiswa1,
    'MAH002':mahasiswa2,
    'MAH003':mahasiswa3
}

print("======================================================================================")
print(f"{'KEY':<15} {'NAMA':<15} {'NIM':<15} {'SKS':<15} {'BEASISWA':<15} {'LAHIR':<15}")   #Membuat Header Table
print("======================================================================================")

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM  = data_mahasiswa[KEY]['nim']
    SKS  = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<15} {NAMA:<15} {NIM:<15} {SKS:<15} {BEASISWA:<15} {LAHIR:<15}")   #Pemanggilan data