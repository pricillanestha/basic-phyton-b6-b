# Tugasnya kerjain di sini kumpul paling lambat jumat 23 April 2021
# cd Tugas-1 untuk imput directory / folder
# cd ../ untuk hapus directory / folder

#Soal 1 (Program yang menerima 3 input dari user)
print ("Mari Bermain Namun, Yuk Kita Kenalan Terlebih dahulu ! ")
Nama_1 = "Alice"
Umur_1 = 15
Tinggi_1 = 160.98
print ("Saya Sistem Dalam Permainan Luas Lingkaran ini dan Nama Saya " +Nama_1+ " ,umur saya" ,Umur_1, "dan tinggi saya" ,Tinggi_1, "Cm.")

# Hanya Tambahan
# Note Pribadi = Penempatan Urutan Syntax berhububngan dengan apa duluan yang akan keluar
Nama_2 = input("Siapa Nama mu ? : ")
print ("Hai ! "+Nama_2+" Salam Kenal !")
Umur_2 = int(input("Berapa Umur mu ? : "))
print ("Oh !, umur mu " ,Umur_2,"tahun." )

#Soal 2 (Program yang dapat menghitung luas lingkaran)
print ("Yuk ! Mulai")
print ("===================")
print ("Masukan jari jari lingkaran : ")
r = int(input(""))
phi = 3.14
L = phi * (r * r)
print ("Luas Lingkaran dengan jari-jari {}, cm adalah {} cm\u00b2" .format(r,L))
print ("Luas Lingkaran dengan jari-jari {}, cm adalah {: .2f} cm\u00b2" .format(r,L))
print ("Selesai, Sampai Jumpa !!!")


#Soal 3 (Program untuk menentukan apakah seorang siswa lulus ujian atau tidak)
print ("======================================")
print ("======================================")
print ("Pengecekan Nilai")
print ("======================================")
print ("Note : KKM 70")

x = float(input("Masukkan Nilai Teori :"))
y = float(input("Masukkan Nilai Praktek :"))

if x and y >= 70 :
    print ("Selamat, anda lulus!")
elif x >= 70 and y < 70 :
    print ("Anda harus mengulang ujian praktek.")
elif x < 70 and y >= 70 :
    print ("Anda harus mengulang ujian teori.")
elif x and y < 70 :
    print ("Anda harus mengulang ujian teori dan praktek.")