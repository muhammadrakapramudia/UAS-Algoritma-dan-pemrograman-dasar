# PROJEK KASIR PECEL LELE
'''Untuk proses penginputan pada mesin kasir perlu memasukkan 
list abjad urutan menu yang tersedia (a,b,c, dan d), kemudian
lanjut ke input jumlah pesan.Jika proses input tidak sesuai 
dengan list menu yang tersedia maka akan muncul notif proses 
input tidak tersedia dan akan di berikan pilihan untuk melanjutkan
order atau tidakJika Y proses akan lanjut ke print invoice yang kosong
dan di alihkan ke tampilan utama kembali untuk bisa melakukan input dari awal.
Jika memilih N proses akan print invoice kosong dan proses selesai.'''

pilihan="y"or"Y"
while pilihan=="y"or"Y":
    print("""
    ===================================================
                    PECEL LELE WONG DESA
        Kp. Cisaat Ds.Kertarahayu Kec. Setu Kab.Bekasi   
    ===================================================
    A. PECEL AYAM                   : Rp. 20.000
    B. PECEL LELE                   : Rp. 17.000
    C. SOTO AYAM                    : Rp. 12.000
    D. ES TEH MANIS                 : Rp. 4.000
    E. TEH TAWAR                    : Rp. 2.000 """)
    print(" \n----- UTAMAKAN MEMBACA DO'A SEBELUM MAKAN------")
    print()
    beli=str(input("MASUKAN LIST ABJAD MENU : "))
    jumlah=int(input("MASUKAN JUMLAH PESANAN ANDA :"))
    if beli =="a" or beli=="A":
        listnama ="PECEL AYAM"
        harga=(20000*jumlah)
        if jumlah >= 5:
            diskon =int(harga*0.2)
            total=int(harga-diskon)
        else:
            diskon =(0)
            total=int(harga)
    elif beli =="b"or beli=="B":
        listnama= "PECEL LELE"
        harga=(17000*jumlah)
        if jumlah >= 5:
            diskon =int(harga*0.2)
            total=int(harga-diskon)
        else:
            diskon =(0)
            total=int(harga) 
    elif beli =="c"or beli == "C":
        listnama= "SOTO AYAM"
        harga=(12000*jumlah)
        diskon=(0)
        total=int(harga)
    elif beli =="d"or beli=="D":
        listnama= "ES TEH MANIS"
        harga=(4000*jumlah)
        diskon=(0)
        total=int(harga)
    elif beli =="e"or beli== "E":
        listnama= "TEH TAWAR"
        harga=(2000*jumlah)
        diskon=(0)
        total=int(harga)
    else:
        listnama = "_"
        harga = "_"
        diskon = "_"
        total = "_"
        pilihan = input("MENU TIDAK TERSEDIA, SILAHKAN MASUKAN ABJAD MENU YANG TERSEDIA SILAHKAN ULANG KEMBALI")
    print("--------------------------")
    print(" PECEL LELE WONG DESA ")
    print("Menu :",listnama)
    print("Jumlah Pesanan :",jumlah)
    print("Harga :",harga)
    print("Diskon :",diskon)
    print("--------------------------")
    print("Jumlah Bayar :",total)
    print("--------------------------")
    pilihan=input("APAKAH ANDA INGIN ORDER KEMBALI Y/N =")


