# Buatlah sebuah program yang dapat menyimpan kontak dan juga menampilkan kontak-kontak
# Terdiri dari nama dan nomor telepon

import csv
csv_filename = 'DaftarContact.csv'

print ("======== Selamat Datang ! ========")
print ("================================")

def create():
    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['NAMA', 'TELEPON']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        nama = input("Nama lengkap: ")
        telepon = input("No. Telepon: ")

        writer.writerow({'NAMA': nama, 'TELEPON': telepon})
        print ("Kontak berhasil ditambahkan")

def show():
    contacts = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")
        for row in csv_reader:
            contacts.append(row)
        print (contacts)
        show_menu()
        
def show_menu():
    print("========= Menu ============")
    print("[1] Daftar Kontak")
    print("[2] Tambah Kontak")
    print("[3] Keluar")
    print("------------------------")
    selected_menu = input("Pilih menu: ")
    
    if(selected_menu == "1"):
        show()
    elif(selected_menu == "2"):
        create()
    elif(selected_menu == "3"):
        print ("Program selesai, sampai jumpa!")
    else:
        print("Menu tidak tersedia")
        show_menu()
        
show_menu()




    



      


    