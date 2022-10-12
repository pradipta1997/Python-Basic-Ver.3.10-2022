#ELIF (ELSE IF) STATEMENT

nama = input("Input nama: ")

if nama == "Pradipta":          # <--Kondisi 1
    print("Hai Pradipta..")     # <--Aksi True 1
elif nama == "Marino":          # <--Kondisi 2
    print("Hai Marino..")       # <--Aksi True 2
elif nama == "Satan":           # <--Kondisi 3
    print("Hai Satan..")        # <--Aksi True 3
elif nama == "Jotep":           # <--Kondisi 4
    print("Hai Jotep..")        # <--Kondisi 4
else:
    print("Nama yang Anda cari tidak ada.") # <--Aksi False

print("End of File")