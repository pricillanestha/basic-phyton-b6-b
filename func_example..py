# Program Example
# Luas = π * r²
# Keliling = π * d // π * 2r

print ("Selamat Datang Di Permainan Menghitung Luas Dan Keliling Lingkaran")
print ("====================================================================")
print ("Masukan Jari-Jari lingkaran : ")
r = int(input(""))
print ("Masukan Diameter lingkaran : ")
d = int(input(""))
phi = 3.14
def luas_lingkaran(r):
    return phi * (r * r)
def keliling_lingkaran(phi, r):
    return 2*phi*r
# print ("Jadi Kalau Luas Lingkaran dengan jari-jari {}, cm adalah {} cm\u00b2" .format(r,luas_lingkaran))
print ("Jadi Kalau Luas Lingkaran dengan jari-jari {}, cm adalah {:.2f} cm\u00b2" .format(r,luas_lingkaran(r)))
print ("====================================================================")
# print ("Jadi Kalau Luas Lingkaran dengan jari-jari {}, cm adalah {} cm\u00b2" .format(r,keliling_lingkaran))
print ("Jadi Kalau Keliling Lingkaran dengan jari-jari {}, cm adalah {:.2f} cm\u00b2" .format(r,keliling_lingkaran(phi, r)))