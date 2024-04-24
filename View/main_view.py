from View import admin_view
from View import donatur_view
from View import penerima_view

def main_program():
    while True:
        try:
            print("""
        +--------------------------------------------------+
        |            PROGRAM SUSTAINABLEHOOD               |
        +--------------------------------------------------+
        | [1] Admin                                        |
        | [2] Donatur                                      |
        | [3] Penerima                                     |
        | [0] Keluar dari Program                          |
        +--------------------------------------------------+
        """)
            pilih = input("Masukkan pilihan (1/2/3/0): ")
            if pilih == "1":
                admin_view.login_admin()
            elif pilih == "2":
                pass
            elif pilih == "3":
                pass
            elif pilih == "0":
                print("+------------------ Terima Kasih ------------------+")
            else:
                print("<< Input tidak valid >>")
        except Exception as e:
            print(f"<< Terjadi kesalahan: {e} >>")

if __name__ == "__main__":
    main_program()