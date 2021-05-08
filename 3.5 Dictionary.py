# DICTIONARY
# dictionary salah satu jenis array di modelkan seperti kamus
# hanya perlu panggil key nya saja tanpa perlu panggil isi nya
# Dictionary di dalamnya ditandai / dipisahkan oleh {}
# Dipanggil berdasarkan name keynya tidak bisa di panggil berdasarkan index
# Menyimpan data secara terstruktur

# List [] (dipanggil berdasarkan index)
# Misal ada Variabel seperti di bawah :
pelanggan_dict = { 
    "nama" : "nafi",
    "umur" :  21,
  # ini key:  #value
}

# List created
# Bisa di panggil berdasarkan index
# pelanggan_list = [    "navi", "grace" ]
pelanggan_list = []

# Change Dictionary
# Merubah nama Navi menjadi Joni
# Sama seperti list klo yang di rubah index klo dictionary dia di rubah keynya
#pelanggan_dict ["nama"] = "Joni"
#pelanggan_dict ["umur"] = "Joni"

# Cara akses dictionary
# print(pelanggan_dict["nama"])
# print(pelanggan_dict["umur"])


# [] list
# {} dctionary
# () fungsi


# input data disctionary
for i in range(3) :
    nama = input ("Masukkan Nama anda : ")
    umur = input ("Masukkan Umur anda : ")
    data = {
        "nama" : nama,
        "umur" : umur,
    }

    pelanggan_list.append(pelanggan_dict)

#print(pelanggan_list[0])
#for i in pelanggan_list :
    print("Nama Pelanggan : ",i["nama"])
    print("Umur Pelanggan : ",i["umur"])

# Kalau mau panggil hanya satu nama saja
# Kalau di simpan di dalam list
# kalau mau panggil menggunakna dictionary berarti harus tau nama keynya apa
data =  pelanggan_list [0]
print ("Nama Pelanggan :", data["nama"])
print ("Nama Pelanggan :", data["umur"])
