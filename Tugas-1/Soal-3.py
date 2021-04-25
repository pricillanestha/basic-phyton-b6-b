#Soal 3 (Program untuk menentukan apakah seorang siswa lulus ujian atau tidak)
print ("======================================")
print ("======================================")
print ("         Pengecekan Nilai             ")
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
else :
    print ("Anda harus mengulang ujian teori dan praktek.")