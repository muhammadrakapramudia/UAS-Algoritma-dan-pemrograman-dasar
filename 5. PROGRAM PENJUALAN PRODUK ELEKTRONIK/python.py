#penjualan produk elektronik

data_product = {
    1:"laptop   ",
    2:"mouse    ",
    3:"monitor  ",
    4:"mouse pad",
    5:"charger  ",
}
daftar_harga = {
    1:200000,
    2:50000,
    3:600000,
    4:30000,
    5:15000,
}

dict_trx = {}
daftar_metode_pembayaran = {
    1: "transfer bank",
    2: "virtual account",
    3: "cash on delivery",
    4: "kartu keredit"
}
print("===============list priduct===============")
for i in data_product:
    print("id product : ",i,"\t nama product :", data_product[i], "\t\t harga product :", daftar_harga[i])
pilih_id = int(input("pilih id product : "))
if pilih_id in data_product:
    pilih_beli = input("ingin beli ? masukan Y: ")
    if pilih_beli == "y" or pilih_beli=="Y":
        nama_penerima    = input("nama penerima : ")
        alamat_penerima  = input("alamat penerima : ")
        telepon          = input("no hp : ")
        kurir_pengiriman = input("kurir pengiriman : ")
        dict_trx = {
            "nama penerima":nama_penerima,
            "alamat penerima":alamat_penerima,
            "No Hp": telepon,
            "Kurir Pengiriman":kurir_pengiriman,
            "prodak id": data_product,
        }
    else:
        pass
    if len (dict_trx) > 0 :
        print("===========metode pembayaran=========")
    for i in daftar_metode_pembayaran:
        print("id : ", i, "\t metode pembayaran : ", daftar_metode_pembayaran[i])
    pilih_metode =int(input("pilih id metode pembayaran :"))
    if pilih_metode in daftar_metode_pembayaran :
        print("Nama Penerima :", dict_trx["nama penerima"])
        print("Alamat Penerima :", dict_trx["alamat penerima"])
        print("No Hp :", dict_trx["No Hp"])
        print("Kurir Kengiriman  :", dict_trx["Kurir Pengiriman"])
        print("product :", data_product[pilih_id])
        print("harga  :", daftar_harga[pilih_id])
        print("Metode Pembayaran :", daftar_metode_pembayaran[pilih_metode])
        konfirmasi= input("apakah anda yakin ingin melakukan pembayaran? (y/n) :")
        if konfirmasi== "y" or konfirmasi == ("Y") :
            print("anda sudah berhasil melakukan pembayaran")
        else:
            print("pembayaran di gagal...")
    else:
        print("id prodak tidak tersedia")