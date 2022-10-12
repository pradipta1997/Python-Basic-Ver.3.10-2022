#MANIPULASI LIST

# RUMUS:
# Table Index = 0(-3) 1(-2) 2(-1) | ->(<-<-<-<-), ->->(<-<-<-), ->->->(<-<-<-)


#MENGAMBIL DATA TERTENTU PADA LIST
mainData = ['Kucing','Marmut','Burung']

data0 = mainData[0]
print(f"Data pertama (index 0): {data0}")

lastData = mainData[-1]
print(f"Data terakhir adalah: {lastData}")

dataHewan = mainData[2]
print(f"Hewan yang terpilih berdasarkan index adalah: {dataHewan}")


#======================================================================
print("===============================================================")


#MENGAMBIL INFO JUMLAH ITEM DATA DALAM LIST (len)
dataLenght = len(mainData)
print(f"Panjang data: {dataLenght}")


#======================================================================
print("===============================================================")


#MENAMBAHKAN ITEM PADA LIST SESUAI POSISI YANG DIINGINKAN (insert)
print(f"Data list lama: {mainData}")

mainData.insert(1,"Semut")  # <--Untuk menambah item baru pad list sesuai nomor index yang diinginkan
print(f"Data list baru sesudah ditambah: {mainData}")

#======================================================================
print("===============================================================")

#MENAMBAHKAN ITEM BARU DIAKHIR PADA LIST (append)
mainData.append("Otter")
print(f"Data list item baru diakhir: {mainData}")


#======================================================================
print("===============================================================")

#MENAMBAHKAN/MENGGABUNGKAN LIST DENGAN LIST (extend)
newData = ["Kura-kura","Musang",'Tikus']
mainData.extend(newData)
print(f"List gabungan: {mainData}")


#======================================================================
print("===============================================================")

#MERUBAH/EDIT DATA PADA LIST SESUAI INDEX MANA YANG DIINGINKAN
mainData[7] = "Kadal"
print(f"Data pada list yang dirubah: {mainData}") 


#======================================================================
print("===============================================================")

#MENGHAPUS DATA (remove)
mainData.remove("Kura-kura")
# mainData.remove("burung") # <--Ini akan error karena penamaan besar kecilnya huruf salah (CamelCase Error)
print(f"Data yang di remove pada list: {mainData}")


#======================================================================
print("===============================================================")

#MENGHAPUS DATA PALING BELAKANG (pop)
dataAkhir = mainData.pop()
print(f"Data terkahir pada list terhapus: {mainData}")
print(f"Data remove: {dataAkhir}")