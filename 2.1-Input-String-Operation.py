# Phyton : USER INPUT
# nama = input("SILAHKAN MASUKAN NAMA KAMU")
# umur = int(input("Berapa umur kamu ? : "))
# print ("Halo, "+nama+ " Salam Kenal Saya Python!")
# print ("oh, ",umur , "Salam kenal aku python, " +nama+ "!")

# Python : String Operation
# Nama_Depan= "Jonathan"
# print (Nama_Depan)
# print(Nama_Depan[1])

# print (Nama_Depan[7:11])
# print (Nama_Depan[7:])
# print (Nama_Depan[:7])
# print(len(nama))

# Python : String Formatting
Nama = "Pricilla"
umur = 22
tinggi = 175.66667

txt_1 = "Nama saya {}, umur saya adalah {}, tinggi saya adalah {} cm" .format(Nama,umur,tinggi)
txt_2 = "Nama saya {}, umur saya adalah {}, tinggi saya adalah {: .2f} cm" .format(Nama,umur,tinggi)
print (txt_1)
print (txt_2)
# txt = "Nama saya {Nama}, umur saya adalah { : .2f}cm" .format(nama, umur, tinggi)