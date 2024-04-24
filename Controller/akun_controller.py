from Model.database import Database
from View import admin_view
from View import donatur_view
from View import penerima_view

class AkunControll:
    def __init__(self):
        self.db = Database()
        self.admin_view = admin_view()
        self.donatur_view = donatur_view()
        self.penerima_view = penerima_view()

    def login_admin_controller(self, username, password):
        admin = self.db.login_admin_model(username, password)
        if admin:
            self.admin_view.login_admin("\n<< Login admin berhasil >>")
            return admin
        else:
            self.admin_view.login_admin("\n<< Login admin gagal >>")
            return None
