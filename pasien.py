# Class Relasi (Association): Pasien
# Beberapa Pasien diperiksa oleh satu Dokter
# Pasien menyimpan referensi ke object Dokter yang memeriksanya

class Pasien:
    # Constructor berparameter
    def __init__(self, id_pasien, nama, umur, gejala):
        if umur < 0:
            raise ValueError("Umur tidak valid")
        if nama.strip() == "" or gejala.strip() == "":
            raise ValueError("Nama dan gejala tidak boleh kosong")
        self.id_pasien = id_pasien   # atribut public
        self.nama = nama
        self.__umur = umur   # atribut private
        self.__gejala = gejala
        self.__diagnosa = "-"          # diisi dokter saat pemeriksaan
        self.__status = "Menunggu"     # Menunggu / Sudah Diperiksa
        self.__dokter = None           # relasi ke object Dokter

# Getter
    def get_umur(self):
        return self.__umur

    def get_gejala(self):
        return self.__gejala

    def get_diagnosa(self):
        return self.__diagnosa

    def get_status(self):
        return self.__status

    def get_dokter(self):
        return self.__dokter

# Method Tambahan
    def ubah_gejala(self, gejala_baru):
        self.__gejala = gejala_baru

    def tetapkan_dokter(self, dokter):
        # satu pasien hanya punya satu dokter
        if self.__dokter is not None:
            return False
        self.__dokter = dokter
        return True

    def terima_diagnosa(self, diagnosa, dokter):
        # diagnosa hanya diterima dari dokter pemeriksa pasien ini
        if dokter is not self.__dokter:
            return False
        if diagnosa.strip() == "":
            return False
        self.__diagnosa = diagnosa
        self.__status = "Sudah Diperiksa"
        return True

    def lepas_dokter(self):
        self.__dokter = None

    def tampilkan_info(self):
        # jika belum punya dokter, akan menampilkan tanda "-"
        if self.__dokter is None:
            nama_dokter = "-"
        else:
            nama_dokter = self.__dokter.nama
        print("Id Pasien :", self.id_pasien)
        print("Nama :", self.nama)
        print("Umur :", self.__umur)
        print("Gejala :", self.__gejala)
        print("Diagnosa :", self.__diagnosa)
        print("Status :", self.__status)
        print("Dokter :", nama_dokter)