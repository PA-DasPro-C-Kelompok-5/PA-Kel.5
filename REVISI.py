from prettytable import PrettyTable
from datetime import datetime
import pwinput, string, random
import json
import os
os.system("cls")
Gacor = os.path.abspath(os.curdir)

# File path for User Data
PathjsonUser = r"C:\Coding\Project Akhir dan tugas\PA Daspro\PA Kel.5 Gacorr\user_data.json"

with open(PathjsonUser, "r") as jsonUser:
    dataUser = json.loads(jsonUser.read())

def tambahUser():
    try:
        with open(PathjsonUser, "r") as jsonUser:
            return json.load(jsonUser)
    except FileNotFoundError:
        return {"Nama": [], "Password": [], "Saldo": []}
    

def simpanUser(data):
    with open (PathjsonUser, "w") as jsonUser:
        json.dump(data, jsonUser, indent=4)

# File path for Data Paket
PathjsonData = r"C:\Coding\Project Akhir dan tugas\PA Daspro\PA Kel.5 Gacorr\data_paket.json"

def clear():
    os.system("cls")

def MembacaData():
    with open(PathjsonData, 'r') as file:
        data_produk = json.load(file)
        return data_produk

def MengupdateData(Data):
    with open(PathjsonData, 'w') as file:
        json.dump(Data, file, indent=4)

# Data Layanan Laundry
jasa = {
    '1': {'Nama': 'Cuci Biasa', 'Harga': 8000},
    '2': {'Nama': 'Setrika Aja', 'Harga': 5000},
    '3': {'Nama': 'Cuci Komplit (Cuci + Setrika)', 'Harga': 15000},
    '4': {'Nama': 'Cuci Express (1 Hari)', 'Harga': 20000},
    '5': {'Nama': 'Cuci Sepatu (Hitam/Putih)', 'Harga': 25000},
    '6': {'Nama': 'Cuci Karpet', 'Harga': 30000}
}

# REGISTER
def register():
    global dataUser 
    while True:
        clear()
        print("+=========================================================+")
        print("| Silahkan Register terlebih dahulu untuk pelanggan baru. |")
        print("+=========================================================+")
        
        username = input("Masukkan Username: ").lower().strip()
        
        # Validasi Username
        if username == "" or all(x.isspace() for x in username):
            print("+====================================+")
            print("| Username tidak boleh berisi spasi! |")
            print("+====================================+")
            continue
        
        # Mengecek apakah Username sudah ada
        if any(user["Username"] == username for user in dataUser ):
            clear()
            print("+=====================+")
            print("| Username sudah ada! |")
            print("+=====================+")
            continue
        
        # Validasi Username
        if not all(x.isalpha() for x in username):
            clear()
            print("+====================================+")
            print("| Username hanya boleh berisi huruf! |")
            print("+====================================+")
            continue
        
        # Validasi Password
        min_pw = 8
        max_pw = 20
        Password = pwinput.pwinput("Masukkan Password: ").strip()
        
        if Password == "":
            clear()
            print("+==============================+")
            print("| Password tidak boleh kosong! |")
            print("+==============================+")
            continue
        
        if all(x.isspace() for x in Password):
            clear()
            print("+====================================+")
            print("| Password tidak boleh berisi spasi! |")
            print("+====================================+")
            continue
        
        limit_pw = len(Password)
        if not (min_pw <= limit_pw <= max_pw):
            clear()
            print("+==================================+")
            print("| Password Min 8, Max 20 Karakter! |")
            print("+==================================+")
            continue
        
        clear()
        print("+=============================================+")
        print("| Password anda benar!, Akun berhasil dibuat! |")
        print("+=============================================+")
        
        # Menyimpan Data Akun Baru
        akun_baru = {"Username": username, "Password": Password, "Saldo": 0}
        dataUser .append(akun_baru) 
        simpanUser (dataUser )
        break

    menu_utama()

def loginUser():
    global username
    users_data = tambahUser()
    if not users_data:
        print("+============================+")
        print("| Data User Tidak Ditemukan! |")
        print("+============================+")
        return False
    
    print("+===============================+")
    print("| LOGIN USER ECO FRAIS' LAUNDRY |")
    print("+===============================+")
    Username = input("Silahkan Masukkan Username Anda:").lower()
    Password = pwinput("Silahkan Masukkan Password Anda: ", "*")

    for user in users_data:
        if user["Username"].lower() == Username:
            if user["Password"] == Password:
                print("+=================================+")
                print("| LOGIN BERHASIL! SELAMAT DATANG! |")
                print("+=================================+")
                return True
            else:
                print("+========================================================+")
                print("| Username atau Password Anda Salah! Silahkan Coba Lagi! |")
                print("+========================================================+")
                return False


'''+==============================================================================================================+'''
'''|                                                                                                              |'''
'''|                                            MENU ADMIN (C R U D)                                              |'''
'''|                                                                                                              |'''
'''+==============================================================================================================+'''


def login_admin():
    print("+=====================+")
    print("|     LOGIN ADMIN     |")
    print("+=====================+")
    if input("Username: ") == "admin" and pwinput.pwinput("Password: ") == "admin123":
        print("+===========================WELCOME==========================+")
        print("| Login berhasil! Selamat datang Admin Eco Frais' Laundry :) |")
        print("+============================================================+")
        menu_admin()
    else:
        print("+==========================INVALID=======================+")
        print("| Username atau password anda salah! Silahkan coba lagi! |")
        print("+========================================================+")

# MENU ADMIN
def menu_admin():
    while True:
        print("+===========================+")
        print("|         MENU ADMIN        |")
        print("+===========================+")
        print("|[1.] Lihat Daftar Jasa     |")
        print("|[2.] Tambahkan Jasa        |")
        print("|[3.] Ubah Jasa             |")
        print("|[4.] Hapus Jasa            |")
        print("|[5.] Kembali Ke Menu Utama |")
        print("+===========================+")

        menu_admin = int(input("Silahkan Masukkan Pilihan Anda: "))
        if menu_admin == 1:
            tampilkan_jasa()
        elif menu_admin == 2:
            tambah_jasa()
        elif menu_admin == 3:
            update_jasa()
        elif menu_admin == 4:
            hapus_jasa()
        elif menu_admin == 5:
            return
        else: 
            print("+===========================INVALID==========================+")
            print("| Pilihan yang anda pilih tidak tersedia! Silakan coba lagi! |")
            print("+============================================================+")
        input("Tekan Enter untuk kembali...")


'''+===================================================================================================================+'''
'''|                                           READ (Menampilkan Daftar Jasa)                                          |'''
'''+===================================================================================================================+'''


# READ
def tampilkan_jasa():
    Data = MembacaData()

    for Kategori in Data["Kategori"]:
        Nama_Kategori = Kategori["Nama Kategori"]
        print(f"\nKategori: {Nama_Kategori}")

        table = PrettyTable()
        table.title = "ECO Frais' LAUNDRY"
        table.field_names = ['No', 'Daftar Jasa', 'Harga (Rp)']
        
        for Paket in Kategori["Paket"]:
            table.add_row([Paket["ID"], Paket["Nama Jasa"], Paket["Harga"]])
        
        print(table)


'''+==============================================================================================================+'''
'''|                                          CREATE (Menambahkan Daftar Jasa)                                    |'''
'''+==============================================================================================================+'''


# CREATE
def tambah_jasa():
    Data = MembacaData()
    tampilkan_jasa()
    print("+======================================================+")
    print("| Silahkan Pilih Kategori Yang Ingin Ditambahkan Jasa: |")
    print("+======================================================+")

    while True:
        print("+========================================+")
        print("| [1.] Menambah Menu Di Kategori Satuan  |")
        print("| [2.] Menambah Menu Di Kategori Komplit |")
        print("| [3.] Menambah Menu Di Kategori Express |")
        print("| [4.] Kembali                           |")
        print("+========================================+")
        Kategori = input("Silahkan Masukkan Pilihan Anda: ")
        
        if Kategori in ['1', '2', '3']:
            break
        elif Kategori == '4':
            return
        else:
            print("+========================= INVALID =======================+")
            print("| Input tidak valid! Silakan masukkan angka yang benar!   |")
            print("+=========================================================+")

    Menu = input("Silahkan Masukkan Menu Jasa Baru: ")

    while True:
        print("+========================================================================+")
        print("| INGAT!!! HARGA PAKET TIDAK BOLEH DI BAWAH 5000 DAN MAKSIMAL 40000 !!!  |")
        print("+========================================================================+")

        try:
            HargaJasa = int(input(f"Masukkan Harga Jasa {Menu}: "))
            if 5000 <= HargaJasa <= 40000:
                print(f"Nama Jasa '{Menu}' Dengan harga {HargaJasa} Berhasil Ditambahkan!")
                break  # Keluar dari loop jika harga valid
            else:
                print("+============================================+")
                print("|  HARGA YANG ANDA MASUKKAN TIDAK SESUAI!!!  |")
                print("+============================================+")
        except ValueError:
            print("+==================================================================+")
            print("| SILAHKAN MASUKKAN DATA YANG VALID DAN JANGAN MENEKAN CTRL + C !!!|")
            print("+==================================================================+")

    new_id = 1
    for item in Data.get("Kategori", []):
        for produk in item.get("Paket", []):
            if produk.get("ID", 0) >= new_id:
                new_id = produk["ID"] + 1

    MenuBaru = {'ID': new_id, 'Nama Jasa': Menu, 'Harga': HargaJasa}

    kategori_map = {
        '1': "Satuan",
        '2': "Komplit",
        '3': "Express"
    }

    kategori_nama = kategori_map[Kategori]

    for item in Data["Kategori"]:
        if item.get("Nama Jasa") == kategori_nama:
            item["Paket"].append(MenuBaru)
            break

    MengupdateData(Data)
    print(" +========================= MENU BERHASIL DITAMBAHKAN =========================+")
    print(f"|             MENU {Menu} Berhasil Ditambahkan dengan ID {new_id}             |")
    print(" +=============================================================================+")


'''+==============================================================================================================+'''
'''|                                        UPDATE (Mengubah Daftar Jasa)                                         |'''
'''+==============================================================================================================+'''


# UPDATE
def update_jasa():
    Data = MembacaData()
    
    while True:
        clear()
        print("+=========================================+")
        print("| [1.] Mengubah Menu di Kategori Satuan   |")
        print("| [2.] Mengubah Menu di Kategori Komplit  |")
        print("| [3.] Mengubah Menu di Kategori Express  |")
        print("| [4.] Kembali                            |")
        print("+=========================================+")
        
        Kategori = input("Silahkan Masukkan Pilihan Anda: ")
        if Kategori == '1':
            Nama_Kategori = "Satuan"
            break
        elif Kategori == '2':
            Nama_Kategori = "Komplit"
            break
        elif Kategori == '3':
            Nama_Kategori = "Express"
            break
        elif Kategori == '4':
            return
        else:
            print("+==============================================================+")
            print("| Kategori Yang Dimasukkan Tidak tersedia! Silahkan Coba Lagi! |")
            print("+==============================================================+")
    
    # Mencari kategori yang dipilih
    kategori_ditemukan = False
    for item in Data["Kategori"]:
        if item.get("Nama Kategori") == Nama_Kategori:
            kategori_ditemukan = True
            print(f"\nKategori: {Nama_Kategori}")
            if not item.get("Paket"):
                print("Tidak ada paket dalam kategori ini.")
                return
            
            for Paket in item.get("Paket", []):
                print(f"ID: {Paket['ID']} | Nama Jasa: {Paket['Nama Jasa']} | Harga: {Paket['Harga']}")

            # Meminta ID paket yang ingin diupdate
            try:
                id_paket = int(input("Masukkan ID Paket yang Ingin Diupdate: "))
            except (ValueError, KeyboardInterrupt):
                print("+==================================================================+")
                print("| SILAHKAN MASUKKAN DATA YANG VALID DAN JANGAN MENEKAN CTRL + C !!!|")
                print("+==================================================================+")
                return

            # Mencari paket berdasarkan ID
            paket_ditemukan = False
            for Paket in item.get("Paket", []):
                if Paket.get("ID") == id_paket:
                    paket_ditemukan = True
                    jasa_baru = input("Masukkan Nama Menu Baru: ")
                    
                    while True:
                        try:
                            print("Minimal harga 5.000")
                            harga_baru = int(input("Masukkan Harga Baru: "))
                            if 5000 <= harga_baru <= 40000:
                                break
                            else:
                                print("+========================================+")
                                print("| Harga Yang Anda Masukkan Tidak Sesuai! |")
                                print("+========================================+")
                        except (ValueError, KeyboardInterrupt):
                            print("+==================================================================+")
                            print("| SILAHKAN MASUKKAN DATA YANG VALID DAN JANGAN MENEKAN CTRL + C !!!|")
                            print("+==================================================================+")
                            return

                    # Update data paket
                    Paket['Nama Jasa'] = jasa_baru
                    Paket['Harga'] = harga_baru
                    MengupdateData(Data)
                    print(f"Nama Jasa '{jasa_baru}' dengan harga '{harga_baru}' Berhasil Diupdate! ")
                    return
            
            if not paket_ditemukan:
                print(f"Properti dengan ID '{id_paket}' tidak ditemukan dalam kategori '{Nama_Kategori}'.")
                return
        
    if not kategori_ditemukan:
        print(f"Tidak Ada Kategori '{Nama_Kategori}' Yang Ditemukan!")


'''+==============================================================================================================+'''
'''|                                           DELETE (Menghapus Jasa)                                            |'''
'''+==============================================================================================================+'''


# DELETE
def hapus_jasa():
    Data = MembacaData()  # Membaca data dari sumber
    tampilkan_jasa()  # Menampilkan jasa yang ada

    while True:
        print("+==============+")
        print("| [1.] Satuan  |")
        print("| [2.] Komplit |")
        print("| [3.] Express |")
        print("| [4.] Kembali |")
        print("+==============+")
        
        Kategori = input("Silahkan Masukkan Pilihan Kategori: ")

        if Kategori == '1':
            Nama_Kategori = "Satuan"
        elif Kategori == '2':
            Nama_Kategori = "Komplit"
        elif Kategori == '3':
            Nama_Kategori = "Express"
        elif Kategori == '4':
            return  # Kembali jika memilih opsi Kembali
        else:
            print("Pilihan kategori tidak valid. Silakan coba lagi.")
            continue  # Kembali ke awal loop jika input tidak valid

        try:
            id_hapus = int(input("Masukkan ID Paket yang Ingin Dihapus: "))
        except ValueError:
            print("ID harus berupa angka!")
            continue  # Kembali ke awal loop jika input tidak valid

        # Mencari kategori yang dipilih
        kategori_ditemukan = False  # Flag untuk mengecek apakah kategori ditemukan
        for kategori in Data.get("Kategori", []):  # Menggunakan .get untuk menghindari KeyError
            if kategori["Nama Kategori"] == Nama_Kategori:
                kategori_ditemukan = True
                list_paket = kategori.get("Paket", [])  # Menggunakan .get untuk menghindari KeyError
                
                # Mencari paket berdasarkan ID
                paket_ditemukan = False  # Flag untuk mengecek apakah paket ditemukan
                for item in list_paket:
                    if item["ID"] == id_hapus:
                        list_paket.remove(item)
                        MengupdateData(Data)  # Mengupdate data setelah penghapusan
                        print(f"Paket dengan ID {id_hapus} berhasil dihapus dari Kategori {Nama_Kategori}.")
                        paket_ditemukan = True
                        break  # Keluar dari loop setelah menemukan dan menghapus paket
                
                if not paket_ditemukan:
                    print(f"Paket dengan ID {id_hapus} tidak ditemukan dalam Kategori {Nama_Kategori}.")
                return  # Keluar dari fungsi setelah mencoba menghapus paket
        
        if not kategori_ditemukan:
            print(f"Kategori {Nama_Kategori} Tidak Ditemukan!")

def update_no_jasa():
    global jasa 
    jasa = {str(i): v for i, (_, v) in enumerate(sorted(jasa.items(), key=lambda x: int(x[0])), start=1)}

def validasi_tanggal(hari, bulan, tahun):
    try:
        datetime.strptime(f"{hari}-{bulan}-{tahun}", "%d-%m-%Y")
        return True
    except ValueError:
        return False

# LOGIN CUSTOMER
def login_customer():
    customers = {
        "Nabil": "00090",
        "Farros": "00085",
        "Hanaya": "00103"
    }
    while True:
        print("+=====================+")
        print("|    LOGIN CUSTOMER   |")
        print("+=====================+")
        username = input("Masukkan Username Customer: ")
        code = pwinput.pwinput("Masukkan Code Customer: ")
        if username in customers and code == customers[username]:
            print(f"Selamat Datang Customer Eco Frais LAUNDRY :), {username}!")
            input("Tekan Enter untuk melanjutkan...")
            menu_customer()
            break
        else:
            print("+========================INVALID========================+")
            print("| Username atau Code Customer salah! Silakan coba lagi! |")
            print("+=======================================================+")
            input("Tekan Enter untuk coba lagi...")


'''+==============================================================================================================+'''
'''|                                                                                                              |'''
'''|                                                 MENU CUSTOMER                                                |'''
'''|                                                                                                              |'''
'''+==============================================================================================================+'''


# MENU CUSTOMER
def menu_customer():
    global username
    while True:
        print("+===============================+")
        print("|[1.] Lihat Daftar Jasa         |")
        print("|[2.] Pesan Jasa                |")
        print("|[3.] Top Up Saldo E-Wallet     |")
        print("|[4.] Cek Saldo E-Wallet        |")
        print("|[5.] Sorting Harga             |")
        print("|[6.] Sorting ID                |")
        print("|[7.] Searching                 |")
        print("|[8.] Kembali ke Menu Utama     |")
        print("+===============================+")

        menu_customer = int(input("Silahkan Masukkan Pilihan: "))
        if menu_customer == 1:
            tampilkan_jasa()
        elif menu_customer == 2:
            pesan_jasa()
        elif menu_customer == 3:
            topup_emoney()
        elif menu_customer == 4:
            ceksaldo_emoney()
        elif menu_customer == 5:
            sort_products()
        elif menu_customer == 6:
            sort_id()
        elif menu_customer == 7:
            search()
        elif menu_customer == 8:
            return
        else:
            print("+========================= INVALID =======================+")
            print("| Input tidak valid! Silakan masukkan angka yang benar!   |")
            print("+=========================================================+")


'''+==============================================================================================================+'''
'''|                                              Pesan Jasa Laundry                                              | '''
'''+==============================================================================================================+'''


def pesan_jasa():
    Data = MembacaData()
    all_services = []

    # Mengumpulkan semua jasa untuk ditampilkan
    for Kategori in Data["Kategori"]:
        for Paket in Kategori["Paket"]:
            all_services.append(Paket)

    # Menampilkan jasa yang tersedia
    print("\nDaftar Jasa yang Tersedia:")
    for service in all_services:
        print(f"ID: {service['ID']} | Nama Jasa: {service['Nama Jasa']} | Harga: Rp {service['Harga']}")

    # Meminta user untuk memilih jasa
    try:
        service_id = int(input("Masukkan ID Jasa yang ingin dipesan: "))
        selected_service = next((service for service in all_services if service['ID'] == service_id), None)

        if selected_service:
            print(f"Anda telah memesan: {selected_service['Nama Jasa']} dengan harga Rp {selected_service['Harga']}")
            # Tambahkan logika untuk memproses pemesanan (misalnya, mengurangi saldo e-wallet, menyimpan pemesanan, dll.)
        else:
            print("ID Jasa tidak ditemukan. Silakan coba lagi.")
    except ValueError:
        print("Input tidak valid! Harap masukkan angka yang benar.")


'''+==============================================================================================================+'''
'''|                                                 TOP UP Saldo                                                 |'''
'''+==============================================================================================================+'''


# TOP UP E-MONEY CUSTOMER
def topup_emoney(username, saldo_cust, login_data):
    while True:
        print("\n+------------TOP UP SALDO-----------+")
        print("| 1. RP. 10.000                     |")
        print("| 2. RP. 25.000                     |")
        print("| 3. RP. 30.000                     |")
        print("| 4. RP. 50.000                     |")
        print("| 5. RP. 100.000                    |")
        print("| 6. Nominal Lain                   |")
        print("+-----------------------------------+")
        
        try:
            pilihan = input("Pilih opsi top-up (1/2/3/4/5/6): ")
            if pilihan in ["1", "2", "3", "4", "5", "6"]:
                if pilihan == "1":
                    jumlah_topup = 10000
                elif pilihan == "2":
                    jumlah_topup = 25000
                elif pilihan == "3":
                    jumlah_topup = 30000
                elif pilihan == "4":
                    jumlah_topup = 50000
                elif pilihan == "5":
                    jumlah_topup = 100000
                elif pilihan == "6":
                    jumlah_topup = int(input("Masukkan nominal yang anda inginkan: "))
                
                if jumlah_topup > 300000:
                    print("+===========================================+")
                    print("| Top-up melebihi batas maksimal (300 Ribu). |")
                    print("+===========================================+\n")
                elif jumlah_topup < 0:
                    print("+=========================================================+")
                    print("| Input nominal tidak valid. Top-up tidak boleh dibawah 0 |")
                    print("+=========================================================+\n")
                else:
                    saldo_cust += jumlah_topup
                    print(f"---Saldo E-Money berhasil ditambahkan sebesar Rp. {jumlah_topup}---")
                    print(f"     Total saldo E-Money anda sekarang adalah Rp. {saldo_cust}     ")
                    
                    for user in login_data:
                        if user["Nama User"].lower() == username.lower():
                            user["Saldo"] = saldo_cust
                            PathjsonData(login_data)
                            
                            with open("emoney.txt", "a") as saldo:
                                print("+=====================================================+", file=saldo)
                                print("|                   TOP UP SALDO                      |", file=saldo)
                                print("+-----------------------------------------------------+", file=saldo)
                                print(f"Username: {username}", file=saldo)
                                print(f"Saldo E-Money berhasil ditambahkan sebesar Rp. {jumlah_topup}", file=saldo)
                                print(f"Total saldo E-Money anda sekarang adalah Rp. {saldo_cust}", end="\n", file=saldo)
                                print("+=====================================================+", file=saldo)
                            break
            else:
                print("+=====================================================+")
                print("| Pilihan tidak valid. Silakan pilih opsi yang benar. |")
                print("+=====================================================+\n")
                
            ulangi = input("Apakah Anda ingin melakukan top-up lagi? (y/t): ")
            if ulangi.lower() == "y":
                continue
            elif ulangi.lower() == "t":
                back = input("Apakah anda ingin kembali ke menu customer? (y/t): ")
                if back.lower() not in ["y", "t"]:
                    print("+======================================================================+")
                    print("| Input tidak valid. Silahkan pilih 'y' untuk ya atau 't' untuk tidak. |")
                    print("+======================================================================+\n")
                elif back.lower() == "y":
                    menu_customer()
                    break
                elif back.lower() == "t":
                    print("\n===================================================\n")
                    print("Masih ingin top up saldo?, silahkan top up kembali")
            else:
                print("+======================================================================+")
                print("| Input tidak valid. Silahkan pilih 'y' untuk ya atau 't' untuk tidak. |")
                print("+======================================================================+\n")
                    
        except (ValueError, KeyboardInterrupt):
            print("\n+=============================================================+")
            print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
            print("+=============================================================+\n")
        except Exception as a:
            print(f"Error, {a}")

'''+==============================================================================================================+'''
'''|                                                Cek Saldo                                                     |'''
'''+==============================================================================================================+'''


def ceksaldo_emoney():
    for user_dict in dataUser:
        if user_dict['username'] == dataUser:
            ceksaldo = user_dict.get("emoney", 0)
            print("SALDO E-Money Anda Tersisa: Rp", ceksaldo)
            break
    else:
        print("Akun tidak ditemukan.")


'''+==============================================================================================================+'''
'''|                                               Cetak Struk Laundry                                            |'''
'''+==============================================================================================================+'''


def cetak_struk_laundry(nama, tgl_pemesanan, jam_pemesanan, tanggal_ambil, nomor_telepon, total_harga, sembarang):
    table = PrettyTable()
    table.field_names = [""]
    table.add_rows([
        [f"Nama Pelanggan: {nama}"],
        [f"Tanggal Pemesanan: {tgl_pemesanan}"],
        [f"Waktu Pemesanan: {jam_pemesanan}"],
        [f"Tanggal Pengambilan: {tanggal_ambil}"],
        [f"Nomor Telepon: {nomor_telepon}"],
        [f"Jumlah Total: Rp {total_harga}"],
        [f"Kode Pelayanan Anda #{sembarang}"],
        ["Silakan Screenshot bukti struk laundry ini."]
    ])
    print(table)
    print("+================================================THANK YOU==========================================================+")
    print("| Terima kasih atas pesanan Anda :) Mohon ambil Laundry Anda pada tanggal pengambilan dengan menunjukkan struk ini. |")
    print("+===================================================================================================================+")

# Example usage
# topup_emoney()
# ceksaldo_emoney()
# cetak_struk_laundry("John Doe", "2023-10-01", "10:00", "2023-10-02", "08123456789", 50000, "123456")


'''=============================================================================================================='''
'''                                        Sorting Produk Berdasarkan Harga                                      '''
'''=============================================================================================================='''


def sort_products():
    data = load_data()
    
    for kategori in data["Kategori"]:
        kategori["produk"] = sorted(kategori["produk"], key=lambda y: y["Harga"])
        
    PathjsonData(data)
    print("\n-------Data telah diurutkan berdasarkan harga-------")
    display_products()
        
    try:
        back = input("Apakah anda ingin mengurutkan kembali berdasarkan ID? (y/t): ").lower()
        while back not in ["y", "t"]:
            print("+======================================================================+")
            print("| Input tidak valid. Silahkan pilih 'y' untuk ya atau 't' untuk tidak. |")
            print("+======================================================================+\n")
            back = input("Apakah anda ingin mengurutkan kembali berdasarkan ID? (y/t): ").lower()
            
        if back == "y":
            sort_id()
        elif back == "t":
            menu_customer()
    except (ValueError, KeyboardInterrupt):
        print("\n+=============================================================+")
        print("|  Mohon masukkan data yang valid dan jangan tekan ctrl + C!  |")
        print("+=============================================================+\n")
    except Exception as a:
        print(f"Error, {a}")


'''=============================================================================================================='''
'''                                          Sorting Produk Berdasrkan ID                                        '''
'''=============================================================================================================='''


def sort_id():
    data = load_data()
        
    for kategori in data["Kategori"]:
        kategori["produk"] = sorted(kategori["produk"], key=lambda x: x["ID"])
        
    PathjsonUser(data)
    print("\n-------Data telah diurutkan berdasarkan ID produk-------")
        
        
    display_products()
    customer()


'''=============================================================================================================='''
'''                                            SEARCH (Mencari Produk)                                           '''
'''=============================================================================================================='''


def search():
    data = load_data()
    cari_produk = input("Masukkan Nama Produk yang akan dicari: ")
    hasil_pencarian = []
    
    for kategori in data["Kategori"]:
        for produk in kategori["produk"]:
            if cari_produk.lower() in produk["Nama Produk"].lower():
                hasil_pencarian.append(produk)
                
    if hasil_pencarian:
        print("Hasil Pencarian:")
        for kategori in data["Kategori"]:
            print(f"\nKategori: {kategori['Nama Kategori']}")
                
            table = PrettyTable()
            table.field_names = ["ID", "Nama Produk", "Harga", "Stok"]
            table.title = "Shopcoolz"
                
            for produk in kategori["produk"]:
                if produk in hasil_pencarian:
                    table.add_row([produk["ID"], produk["Nama Produk"], produk["Harga"], produk["Stok"]])
                    
            print(table)
    else:
        print("\n----Produk tidak ditemukan----.")
        
    return hasil_pencarian


# MAIN MENU
def menu_utama():
    while True:
        print("+======HELLO==============================================================================+")
        print("|                                  [Eco Frais' LAUNDRY]                                   |")
        print("|     | ASSALAMUALAIKUM WARAHMATULLAHI WABARAKATUH! | SELAMAT DATANG! |  WELCOME! |       |")
        print("+==============================================================================LAUNDRY====+")

        print("+==========================+")
        print("| Silakan Pilih Role Anda: | \n|[1.] Register             |\n|[2.] Admin                |\n|[3.] Customer             |\n|[4.] Keluar               |")
        print("+==========================+")
        pilihan = input("| Pilih (1-4):  |")
        if pilihan == "1": register()
        elif pilihan == "2": login_admin()
        elif pilihan == "3": login_customer()
        elif pilihan == "4":
            print("+==================================THANK YOU==================================+")
            print("| Terima kasih atas kunjungan Anda di Eco Frais' LAUNDRY!, Sampai Jumpa lagi! |")
            print("+=============================================================================+")
            break
        else:
            print("+============================INVALID============================+")
            print("| Pilihan yang anda masukkan tidak tersedia! Silakan coba lagi! |")
            print("+===============================================================+")

menu_utama()
