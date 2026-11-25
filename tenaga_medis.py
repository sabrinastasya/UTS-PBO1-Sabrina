# TenagaMedis merupakan Superclass
# Class induk yang menyimpan data umum tenaga medis
# Class Dokter dan Perawat mewarisi class ini (inheritance)

class TenagaMedis:   
    # Constructor berparameter
    def __init__(self, id_tm, nama, umur):
        # validasi data awal
        if umur <= 0:
            raise ValueError("Umur tidak valid")
        if nama.strip() == "":
            raise ValueError("Nama tidak boleh kosong")
        self.nama = nama   # atribut public bisa diakses langsung
        self.__id = id_tm   # atribut private, hanya bisa diakses lewat method
        self.__umur = umur
        self.__aktif = True

# Getter: membaca atribut private
    def get_id(self):   
        return self.__id

    def get_nama(self):
        return self.nama

    def get_umur(self):
        return self.__umur

    def is_aktif(self):
        return self.__aktif
    
# Method Tambahan 
    def ubah_umur(self, umur_baru):
        self.__umur = umur_baru

    def ubah_status(self):
        self.__aktif = not self.__aktif
        return self.__aktif

    def get_peran(self):
        return "Tenaga Medis"   # di override oleh subclass

    def tampilkan_info(self):   # menampilkan data umum
        if self.__aktif:
            status = "Aktif"
        else:
            status = "Nonaktif"
        print("Tenaga Medis :", self.get_peran())
        print("Id :", self.__id)
        print("Nama :", self.nama)
        print("Umur :", self.__umur)
        print("Status :", status)

