from tenaga_medis import TenagaMedis

# import TenagaMedis sebagai Superclass
# Subclass 2: Perawat
# Mewarisi id, nama, umur, status dari TenagaMedis

class Perawat(TenagaMedis):
    # Constuctor berparameter
    def __init__(self, id_tm, nama, umur, shift, ruangan):
        # memanggil constructor superclass untuk data umum
        super().__init__(id_tm, nama, umur)
        if shift not in ("Shift Pagi", "Shift Siang", "Shift Malam"):
            raise ValueError("Shift tidak valid")
        self.__ruangan = ruangan   # atribut private
        self.__shift = shift 
        self.__jumlah_tugas = 0 # jumlah tugas yang sudah dikerjakan

# GETTER 
    def get_ruangan(self):
        return self.__ruangan

    def get_shift(self):
        return self.__shift

    def get_jumlah_tugas(self):
        return self.__jumlah_tugas

# Method Tambahan
    def ganti_shift(self, shift_baru):
        if shift_baru not in ("Shift Pagi", "Shift Siang", "Shift Malam"):
            return False
        self.__shift = shift_baru
        return True

    def catat_tugas(self):
        # menambah hitungan tugas yang sudah dikerjakan
        self.__jumlah_tugas += 1

# Override 
    def get_peran(self):
        return "Perawat"

    def tampilkan_info(self):
        super().tampilkan_info() # tampilkan data umum dari TenagaMedis dulu
        print("Shift :", self.__shift)
        print("Ruangan :", self.__ruangan)
        print("Jumlah Tugas :" , self.__jumlah_tugas)