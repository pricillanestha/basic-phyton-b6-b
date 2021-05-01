# Function Parameter / Argument

def Sapa() :
 print ("Hello")

def say_hay() :
 print ("Hai")

def tanya_kabar() :
 print ("Apa Kabar ?")

def perkenalan (nama,umur) :
 print ("Nama saya adalah " +nama)
 print ("Nama saya adalah " ,umur)
# perkenalan("Nafi",22)
# perkenalan("Jon",23)
# perkenalan("Joni",24)

# Bisa di isikan lebih dari satu parameter

#Jika di isikan oleh user
nama = input ("Masukkan nama kamu : ")
umur = int(input ("Masukkan nama kamu : "))
perkenalan(nama,umur)

# FUNCTION DEFAULT PARAMETER
def perkenalan (nama,umur) :
# print ("Nama saya adalah " +nama)
# print ("Nama saya adalah " +umur)
#                            : Perhatikan bagian
# nama = input ("Masukkan nama kamu : ")
# umur = input ("Masukkan nama kamu : "))
# perkenalan(nama,umur)
