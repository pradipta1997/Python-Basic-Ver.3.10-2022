#TEKNIK MENDUPLIKAT LIST

#main data
a = ["Apel","Belimbing","Ceri","Durian","Enau"]
print("Data var a: ", a)

b = a   # <--Method variable seperti ini namanya (Pass by refered)
print("Data var b: ", b)

#kita akan merubah member dari variable a
a[3] = "Duku"   # <--ini akan merubah kedua list di variable a & b secara bersamaan, karena menggunakan data yg sama.
b.sort()
print("a = ", a)
print("b = ", b)

#cek address list a & b
print("Address a = ", hex(id(a))) # <-- ternyata address a & b sama, itulah mengapa disaat merubah member/item pada
print("Address b = ", hex(id(b))) # list a maka list b ikut berubah hal yang sama juga.


#============================================================================================================
print("==========================================================")


#MENDUPLIKASI LIST DENGAN COPY (.copy()) / full duplicate
print("MEMBUAT LIST C DENGAN COPY LIST A \n")
c = a.copy()    # <-- variable c, mengcopy data dari variable a, sehingga kalau var c dirubah var a tidak ikut terubah

print("Address a = ", hex(id(a)))
print("Address b = ", hex(id(b)))
print("Address c = ", hex(id(c))) # <--Disini address c sudah berbeda dari a & b.
print("\n")

print("Merubah data index 3 di variable c")
c[3] = "Durian"
print("Data variable c = ", c)
print("Data variable b = ", b)
