# FUNCTION RETURN VALUE
# Digunakan untuk mengembalikan nilai yg ada di suatu function
# Jadi ga perlu pakai print
# bisa dilakukan pengolahan lagi
# Menampilkan nilai asli
# akan selalu mengembalikan tipe data sesuai dengan aslinya

def luas_kotak(p,l) :
    return p*l

def keliling_kotak(p,l) :
    keliling = p+p+l+l
    text = "kelilingnya adalah  {}".format(keliling) 
    return text
# Menampilkan tipe data asli

def luas_kotak_string(p,l) :
    luas = p*l
    print(luas)
# Akan selalu mengembalikan nilai tipe data sesuai isi
# Print = hanya untuk menampilkan

print (luas_kotak(5,3)*2)
print (keliling_kotak(5,10)*2)
luas_kotak_string(5,30)