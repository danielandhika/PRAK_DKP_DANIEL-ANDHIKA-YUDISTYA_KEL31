print("Kelompok         : 31")
print("Shift            : 2")
print("Nama Anggota 1   : Michelia Vadilla Verdianto	 (21120120120020)")
print("Nama Anggota 2   : Donny Ridwan Setiawan (21120120130083)")
print("Nama Anggota 3   : Muhammad Ghulam Abdul Nashr Umar (21120120120029)")
print("Nama Anggota 4   : Daniel Andhika Yudistya (21120120140048)")

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
