from Controller.akun_controller import AkunControll

akun = AkunControll()

def login_admin():
    while True:
        try:
            print("""
+--------------------------------------------------+
|                  LOGIN DONATUR                   |
+--------------------------------------------------+""")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            akun.login_admin_controller(username, password)
            break
        except Exception as e:
            print(f"<< Terjadi kesalahan: {e} >>")

def menu_admin():
    while True:
        try:
            print("""
+--------------------------------------------------+
|            PROGRAM SUSTAINABLEHOOD               |
|               MENU UTAMA DONATUR                 |
+--------------------------------------------------+
| [1] Buat Donasi                                  |
| [2] Tampilkan Daftar Donasi dan Barang           |
| [3] Perbarui Donasi                              |
| [4] Hapus Donasi                                 |
| [5] Urut Daftar Donasi dan Barang                |
| [6] Cari Daftar Donasi dan Barang                |
| [0] Kembali                                      |
+--------------------------------------------------+""")
            pilih = input("Masukkan pilihan (1/2/3/0): ")
            if pilih == "1":
                pass
            elif pilih == "2":
                pass
            elif pilih == "3":
                pass
            elif pilih == "4":
                pass
            elif pilih == "5":
                pass
            elif pilih == "6":
                pass
            elif pilih == "0":
                print("<< Kembali ke menu utama >>")
            else:
                print("<< Input tidak valid >>")
        except Exception as e:
            print(f"<< Terjadi kesalahan: {e} >>")