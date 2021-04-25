# FUNCTION
# Di tandai dengan penggunaan 
# def di awal - nama function - parameter - : (titik 2)
#  kemudian isinya

# Contoh :
# def my_function() :
#  print ("Hello")

# my_function()
# Bisa dilakukan berkali kali tapi yang di ulang my_function()

# my_function()
# my_function()
# my_function()
# my_function()

def Sapa() :
 print ("Hello")
def say_hay() :
 print ("Hai")
def tanya_kabar() :
 print ("Apa Kabar ?") 

print ("Hai Bro !")
jawab = int(input("Masukkan Jawaban !"))
if (jawab == 1) :
    Sapa()
elif (jawab == 2) :
    say_hay()
elif (jawab == 3) :
    tanya_kabar()
