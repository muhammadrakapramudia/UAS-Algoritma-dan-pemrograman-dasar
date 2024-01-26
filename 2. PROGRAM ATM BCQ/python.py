user = {
    'pin': 1234,
    'saldo':100000000
}

def uang_tunai(): # def untuk mendefinisikan fungsi dan memberikan kode yang akan dijalankan ketika fungsi tersebut dipanggil.
    while True:
        jumlah = int(input("Masukkan jumlah uang yang ingin Anda tarik : "))
        if jumlah > user['saldo']:
            print("Anda tidak memiliki saldo yang cukup untuk melakukan penarikan tunai ")
        else:
            user['saldo'] = user['saldo'] - jumlah
            print(f"Rp.{jumlah} berhasil ditarik, sisa saldo Anda adalah Rp.{user['saldo']} ")
            print('')
            return False
          #(KEMBALI)
        
def saldo():
    print(f"Total saldo Rp.{user['saldo']} ")
    print('')


pilihan = False

print('')
print("Selamat datang di ATM BCQ")
print('====================================================')
pin = int(input('Silakan masukkan empat digit pin Anda: '))
if pin == user['pin']:
    while pilihan == False:
        print("apa yang ingin kamu lakukan ?")
        print(" Masukkan 1. Tarik Tunai \n Masukkan 2. Info saldo \n Masukkan 3. Keluar")

        pertanyaan = int(input("Masukkan nomor yang sesuai dengan aktivitas yang ingin Anda lakukan: "))

        if pertanyaan == 1:
            uang_tunai()
        elif pertanyaan == 2:
            saldo()
        elif pertanyaan == 3:
            pilihan = True

        else:
            print("Silakan masukkan nilai yang benar yang ditampilkan...")
else:
    print("Salah memasukkan pin")