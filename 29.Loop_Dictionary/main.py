#LOOPING IN DICTIONARY

#MAIN DATA
teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasyep",
    "cuy":"ucuy surucuy"
}

#LOOPING FIRST TRY (yang keluar adalah key-nya saja)
for i in teman_teman:
    print(i)

#=====================================================
print("=============================================")

#OPERATOR UNTUK MENGAMBIL KEY ITERABLES
keys = teman_teman.keys()   # <--Untuk mengambil keys/iterables[] saja
print(keys)

#=====================================================
print("=============================================")

#LOOPING & MENGAMBIL VALUES ITERABLES
values = teman_teman.values()   # <--Untuk mengambil values/iterables[] saja
print(values)

#=====================================================
print("=============================================")

#LOOPING & MENGAMBIL VALUES NYA
for key in teman_teman.keys():
    print(teman_teman.get(key)) # <--Untuk mengambil values saja dengan .get()

for i in teman_teman.values():  # <--Sama saja seperti cara diatas/cara lain mengambil value saja
    print(i)

#=====================================================
print("=============================================")

#MENGAMBIL ITEM ITERABLES []
items = teman_teman.items() # <--Untuk mengambil item iterables []
print(items)

#=====================================================
print("=============================================")

#LOOPING MENGAMBIL KEY & VALUE ITEMS
for item in teman_teman.items():
    print(item)

#=====================================================
print("=============================================")

#
for key,value in teman_teman.items():
    print(f"[Key] = {key} [Value] = {value}")