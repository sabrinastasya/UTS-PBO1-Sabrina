from tenaga_medis import TenagaMedis

# import TenagaMedis sebagai Superclass
# Subclass 1: Dokter (extends TenagaMedis)
# Mewarisi id, nama, umur, status dari TenagaMedis
# Relasi: satu Dokter memeriksa beberapa Pasien (association)

class Dokter(TenagaMedis):
    # Constuctor berparameter
    def __init__(self, id_tm, nama, umur, spesialis, jam_praktik):
        # memanggil constructor superclass, hanya mengirim data milik TenagaMedis
        super().__init__(id_tm, nama, umur)
        self.__spesialis = spesialis   # atribut private
        self.__jam_praktik = jam_praktik  
        self.__daftar_pasien = [] # menyimpan banyak object Pasien (relasi)

# Getter: membaca atribut private
    def get_spesialis(self):
        return self.__spesialis

    def get_jam_praktik(self):
        return self.__jam_praktik

    def get_daftar_pasien(self):
        return self.__daftar_pasien

    def get_jumlah_pasien(self):
        return len(self.__daftar_pasien)

# Method Tambahan
    def ubah_spesialis(self, spesialis_baru):
        self.__spesialis = spesialis_baru

    def tambah_pasien(self, pasien):   # relasi: dokter menerima pasien
        if not self.is_aktif():
            return False
        if pasien.get_dokter() is not None:
            return False               # pasien sudah punya dokter
        self.__daftar_pasien.append(pasien)
        pasien.tetapkan_dokter(self)   # pasien juga mengetahui dokternya
        return True

    def periksa_pasien(self, pasien, diagnosa):
        # dokter hanya boleh memeriksa pasien miliknya sendiri
        if not self.is_aktif():
            return False
        if pasien not in self.__daftar_pasien:
            return False
        return pasien.terima_diagnosa(diagnosa, self)

    def hapus_pasien(self, pasien):
        if pasien in self.__daftar_pasien:
            self.__daftar_pasien.remove(pasien)
            pasien.lepas_dokter()
            return True
        return False

# OVERRIDE (menimpa method superclass)
    def get_peran(self):
        return "Dokter"

    def tampilkan_info(self):
        super().tampilkan_info() # tampilkan data umum dari TenagaMedis dulu
        print("Spesialis: ", self.__spesialis)
        print("Jam Praktik :", self.__jam_praktik)
        print("Jumlah Pasien :", len(self.__daftar_pasien))
    

    