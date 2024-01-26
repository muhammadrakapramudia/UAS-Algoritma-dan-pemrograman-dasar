print('          PT.MAKMUR ABADI           ')
print('================================================')
print('Program Penggajian Karyawan')
print('Nama Karyawan')
print('Golongan A/B/C/D(pilih sesuai golongan karyawan)')
print('================================================')
print()
 
# proses input
 
nama = input('Nama Karyawan: ')
golongan = input('Golongan: ')
jam_kerja = int(input('Jumlah jam kerja: '))
 
print()
 
# tentukan jumlah upah per jam berdasarkan golongan
 
if golongan == "a"or golongan=="A":
  upah_per_jam = 5000
elif golongan == "b" or golongan=="B":
  upah_per_jam = 7000
elif golongan == "c" or golongan=="C":
  upah_per_jam = 8000
elif golongan == "d" or golongan=="D":
  upah_per_jam = 10000

total_upah =(jam_kerja * upah_per_jam)
  
# cek apakah jam kerja lebih dari 48 jam
if (jam_kerja - 48) > 0:
  new_var = total_upah = total_upah + ((jam_kerja - 48)*4000)
  new_var

# proses output
print(nama,'menerima upah Rp.',total_upah,'per minggu')