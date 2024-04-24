class Donasi:
    def __init__(self, data):
        self.donasi = {"id_donasi": data[0],
                    "status": data[1],
                    "jumlah": data[2],
                    "tanggal": data[3],
                    "id_barang": data[4],
                    "id_penerima": data[5],
                    "id_donatur": data[6],
                    "id_admin": data[7]
                    }