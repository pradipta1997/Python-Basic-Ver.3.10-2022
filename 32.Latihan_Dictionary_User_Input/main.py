#LATIHAN DICTIONARY (USER INPUT)

#PACKAGES PYTHON
import datetime # <--Package untuk waktu/penanggalan
import os       # <--Package untuk membersihkan konsol atau (cls)

#DATA TEMPLATE
mahasiswa_template = {
    'nim':'000000',
    'nama':'nama',
    'sks_lulus':0,
    'tgl_lahir':datetime.datetime(1111,1,11)
}


#MEMBUAT DICTIONARY KOSONG
data_mahasiswa = {}

while True:

    os.system("cls")    # <--Untuk membersihkan konsol secara otomatis
    print(f"{'DATA MAHASISWA':^20}")    # <-- Title
    print("="*20)

    mahasiswa_input = dict.fromkeys(mahasiswa_template.keys()) #<--Untuk mengambil data berdasarkan keys di mahasiswa_template
    # print(mahasiswa_input)  # <--Data yang diambil berdasarkan keys masih kosong/none. Karena belum diinput user.
    mahasiswa_input['nim'] = input("NIM Mahasiswa: ")   # <--Input data nim
    mahasiswa_input['nama'] = input("Nama Mahasiswa: ") # <--Input data nama
    mahasiswa_input['sks_lulus'] = int(input("SKS Lulus Mahasiswa: "))  # <--Input data sks

    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))    # <--Input data tahun
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))    # <--Input data bulan
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31): "))# <--Input data tanggal
    mahasiswa_input['tgl_lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    # print(mahasiswa_input)  # <--Data yang sudah diinput sudah terisi pada masing-masing keys.


    data_mahasiswa.update({'key':mahasiswa_input})  # <--Update data mahasiswa_input berdasarkan key

    print("======================================================================================")
    print(f"{'KEY':<15} {'NIM':<15} {'NAMA':<15} {'SKS LULUS':<15} {'TANGGAL LAHIR':<15}") #Membuat Header Table
    print("======================================================================================")

    for mahasiswa_input in data_mahasiswa:
        KEY = mahasiswa_input

        NIM = data_mahasiswa[KEY]['nim']
        NAMA = data_mahasiswa[KEY]['nama']
        SKS_LULUS = data_mahasiswa[KEY]['sks_lulus']
        TGL_LAHIR = data_mahasiswa[KEY]['tgl_lahir'].strftime("%x")

        print(f"{KEY:<15} {NIM:<15} {NAMA:<15} {SKS_LULUS:<15} {TGL_LAHIR:<1}")

    print("\n")
    is_done = input("Apakah ingin lanjut (y/n) ?")
    if is_done == "n":
        break

print("Akhir baris program..")

