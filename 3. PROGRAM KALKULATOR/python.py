# program kalkulator

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b
    
def modulo(a, b):
    return a % b
    
def pangkat(a, b):
    return a ** b
    
#hasil bagi contohnya: misal 10/4 hasilnya 2 saja, bukan 2.5, intinya desimalnya dibuang
def hasilbagi(a, b):
    return a // b

print('\n   Kalkulator    ')
print('===================')
print("\nPilih Perhitungan:")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
print("5.Modulo")
print("6.Pangkat")
print("7.Hasilbagi")
print('====================')
while True:
    pilihan = input("\nPilih Nomor : ")
    
    if pilihan in ('1', '2', '3', '4', '5', '6', '7'):
        inputan1 = int(input("Input angka pertama: "))
        inputan2 = int(input("Input angka kedua: "))


        if pilihan == '1':
            print(inputan1, "+", inputan2, "=", tambah(inputan1, inputan2))

        elif pilihan == '2':
            print(inputan1, "-", inputan2, "=", kurang(inputan1, inputan2))

        elif pilihan == '3':
            print(inputan1, "*", inputan2, "=", kali(inputan1, inputan2))

        elif pilihan == '4':
            print(inputan1, "/", inputan2, "=", bagi(inputan1, inputan2))
            
        elif pilihan == '5':
            print(inputan1, "%", inputan2, "=", modulo(inputan1, inputan2))
            
        elif pilihan == '6':
            print(inputan1, "**", inputan2, "=", pangkat(inputan1, inputan2))
            
        elif pilihan == '7':
            print(inputan1, "//", inputan2, "=", hasilbagi(inputan1, inputan2))
        
        # Cek apakah mau menghitung lagi dengan ketik "ya"
        # break atau hentikan dengan ketik "tidak"
        reset = input("\nMau menghitung lagi? (ya/tidak): ")
        if reset == "tidak":
          break 
    else:
        print("Inputan salah")