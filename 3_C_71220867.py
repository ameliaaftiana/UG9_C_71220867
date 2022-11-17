print("========== CATATAN BELANJA ==========")
print("========== Daftar 1 ==========")
print ("Daftar Belanja 1: ['Sikat Gigi', 'Odol', 'Shampoo', 'Sabun', 'Ciduk']")
print ("========== Daftar 2 ==========")
print ("Daftar Belanja 2: ['Teh', 'Gula', 'Garam', 'Micin', 'Kecap']")
print ("Jawab dengan angka [1/21]")
print ("1. Rubah Belanjaan")
print ("2. Keluar")
#data
daftar11='Sikat Gigi', 'Odol', 'Shampoo', 'Sabun', 'Ciduk'
daftar12='Teh', 'Gula', 'Garam', 'Micin', 'Kecap'
#input
pilihan=int(input("Masukkan Pilihan:"))
daftar1=str(input("Masukkan nama item ke dafatr 1:"))
index1=int(input("Masukkan index yang ingin dirubah:"))
daftar2=str(input("Masukkan nama item ke daftar 2:"))
index2=int(input("Masukkan index yang ingin dirubah:"))
print ("========== Daftar 1 ==========")
print ("Daftar Belanja 1:",daftar11[index1])
print ("========== Daftar 2 ==========")
print ("Daftar Belanja 2:",daftar12[index2])
