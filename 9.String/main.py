#PENGENALAN TIPE DATA STRING

data = "Ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. Dengan menggunakan single quote '...'
    2. Dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

data = '"Hallo, apa kabar?"'    # <-- yang ditampilkan adalah kutip 2
print(data)
data = "'Hallo, apa kabar?'"    # <-- yang ditampilkan adalah kutip 1
print(data)
data = "Ini hari Jum'at"        # <-- dengan menggunakan double quote agar koma atas pada nama hari tidak di hitung
print(data)

print("===================================")


# 2. Menggunakan tanda (\)

'''
Menggunakan tanda (\) agar--> (') menjadi string
tanpa harus menggunakan teknik double quote
'''

data = 'Ini adalah hari Jum\'at'
print(data)
data = 'G\'day, isn\'t it?'
print(data)

print("===================================")


# 3. Menggunakan Backslash (\\)

''''
    Ini digunakan misal pada saat kita ingin
    memasukan url link/folder direktori
'''

data = "C:\\Users\\Pradipta"    # <-- Menggunakan tanda double backslash agar terbaca slash nya
print(data)

print("===================================")


# 4. Menggunakan Tab (\t)

'''
Agar string berjarak atau berjauhan
'''

data = "Pradipta\tRamadhan"
print(data)

print("===================================")


# 5. Menggunakan backspace (\b)

'''
Agar string saling berdekatan atau menempel
'''

data = "Pradipta\bRamadhan"
print(data)

print("===================================")


# 6. Menggunakan newline (\n)

'''
    Agar membuat baris baru di bawah string awal.

    List:
        1. LF (Line Feed), biasanya digunakan pada OS [Unix,MacOs, Linux].
        2. CR (Carriage Return), biasanya digunakan pada OS [Commodore, Acorn, Lisp]
        3. CRLF (Carriage Return Line Feed), biasanya digunakan pada OS [Windows]

'''

data = "Ini adalah baris pertama.\nIni adalah baris kedua." # <-- LF (Line Feed)
print(data)

data = "Ini adalah baris pertama.\rIni adalah baris kedua." # <-- CR (Carriage Return)
print(data)

data = "Ini adalah baris pertama.\r\nIni adalah baris kedua." # <-- CRLF (Carriage Return Line Feed)
print(data)

print("===================================")


# 7. Menggunakan String Literal dan Raw String (r)

data = 'C:\new folder'  #<-- contoh tidak menggunakan (raw string) maka dalam penulisan path akan salah
print(data)

data = (r'C:\new folder')   #<-- harus menambahkan r(raw string) sebelum string agar penulisan path benar
print(data)

print("===================================")


# 8. Menggunakan Multiline Literal String ("""...""")
data = """
        Nama      : Pradipta Ramadhan
        TTL       : Aceh, 30 Januari 1997
        Pekerjaan : IT Konsultan
    """
print(data)

print("===================================")


# 9. Menggunakan Multiline Literal String & Raw ("""...""" & r)
data = (r"""
        Nama      : Pradipta Ramadhan
        TTL       : Aceh, 30 Januari 1997
        Pekerjaan : IT Konsultan
        Website   : www.pradiptaramadhan.com\new files
    """)
print(data)