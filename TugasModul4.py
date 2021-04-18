import Method

nama=Method.ticket_method("Nama")
nama.intro(31)

print(" ______________________________________ ")
print("|   SELAMAT DATANG DI TEKKOM AIRWAYS   |")
print("|______________________________________|")
print("|         RUTE            |    Harga   |")
print("|1. JAKARTA-PALANGKARAYA  | Rp 800.000 |")
print("|2. JAKARTA-SURABAYA      | Rp 650.000 |")
print("|3. JAKARTA-SEMARANG      | Rp 550.000 |")
print("|______________________________________|")

def book():
	pax = int(input("Jumlah Penumpang = "))
	print ("Masukan nama Penumpang : ")
	for i in range (int(pax)):
		i += 1
		n = input("Penumpang ke- {} ".format(i))
	tot=pax*harga
	print("Total Harga Rp ",tot)
	print("__________")
	email=input("Masukkan Alamat Email Anda: ")
	print("----------")
	print("Terima Kasih Telah Memilih Terbang Bersama Kami")
	print("E-Ticket Anda Akan Dikirimkan Melalui Email ", email)
	print("<<<Tetap Patuhi Protokol Kesehatan>>>")
	print("----------")
rute= int(input("Masukkan Pilihan Rute : "))
if (rute == 1):
	harga=800000
	book()
elif (rute == 2):
	harga=650000
	book()
elif (rute == 3):
	harga=550000
	book()
else:
	print("Tidak Ada Pilihan Rute Tersebut.")
