#DATE & TIME

import datetime as dt

#MENGINDENTIFIKASIKAN TANGGAL HARI INI
today = dt.date.today() # <-- date ini adalah tipe datanya | today() untuk mengindentifikasi hari ini
print(today)

#=======================

#MENGUBAH TANGGAL KE NAMA HARI
tanggal = dt.date(1997,1,30)
print(tanggal)
print(f"Hari ini adalah hari: {tanggal:%A}")