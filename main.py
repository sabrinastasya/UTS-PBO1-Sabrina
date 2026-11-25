from dokter import Dokter
from perawat import Perawat
from pasien import Pasien

# Membuat object (instance dari class)
pasien1 = Pasien("PS01", "Tasya", 10, "Tipes")
pasien2 = Pasien("PS02", "David", 20, "Asma")

dokter1 = Dokter("D01", "dr. Vio", 35, "Spesialis Anak", "10.00-12.00")
dokter2 = Dokter("D02", "dr. Rei", 40, "Spesialis Umum", "12.00-13.00")

perawat1 = Perawat("P01", "Febi", 25, "Shift Malam", "Ruang 1")
perawat2 = Perawat("P02", "Poy", 24, "Shift Siang", "Ruangan 2")

# Relasi: dokter memeriksa pasien 
dokter1.tambah_pasien(pasien1)
dokter2.tambah_pasien(pasien2)

# Penyimpanan data (list berisi object)
daftar_dokter = [dokter1, dokter2]
daftar_perawat = [perawat1, perawat2]
daftar_pasien = [pasien1, pasien2]


def input_angka(pesan):
    # meminta input angka, mengulang sampai input valid
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input harus berupa angka!")

def cari_tenaga(daftar, id_cari):
    # mencari dokter/perawat berdasarkan id (tidak peka huruf besar/kecil)
    for t in daftar:
        if t.get_id().lower() == id_cari.lower():
            return t
    return None

def cari_pasien(id_cari):
    # mencari pasien berdasarkan id
    for p in daftar_pasien:
        if p.id_pasien.lower() == id_cari.lower():
            return p
    return None

def pilih_kategori():
    print("1. Dokter\n2. Perawat\n3. Pasien")
    return input_angka("Pilih kategori: ")


# ---------------- 1. TAMBAH DATA ----------------
def tambah_data():
    print("\n--- TAMBAH DATA ---")
    k = pilih_kategori()
    if k == 1:
        id_ = input("Id dokter: ")
        if cari_tenaga(daftar_dokter + daftar_perawat, id_):
            print("Id sudah dipakai!")
            return
        nama = input("Nama: ")
        umur = input_angka("Umur: ")
        spesialis = input("Spesialis: ")
        jam = input("Jam praktik: ")
        try:
            daftar_dokter.append(Dokter(id_, nama, umur, spesialis, jam))
        except ValueError as e:
            print("Gagal menambahkan dokter:", e)
            return
        print("Dokter berhasil ditambahkan.")
    elif k == 2:
        id_ = input("Id perawat: ")
        if cari_tenaga(daftar_dokter + daftar_perawat, id_):
            print("Id sudah dipakai!")
            return
        nama = input("Nama: ")
        umur = input_angka("Umur: ")
        shift = input("Shift: ")
        ruangan = input("Ruangan: ")
        try:
            daftar_perawat.append(Perawat(id_, nama, umur, shift, ruangan))
        except ValueError as e:
            print("Gagal menambahkan perawat:", e)
            return
        print("Perawat berhasil ditambahkan.")
    elif k == 3:
        id_ = input("Id pasien: ")
        if cari_pasien(id_):
            print("Id sudah dipakai!")
            return
        nama = input("Nama: ")
        umur = input_angka("Umur: ")
        gejala = input("Gejala: ")
        try:
            pasien = Pasien(id_, nama, umur, gejala)
        except ValueError as e:
            print("Gagal menambahkan pasien:", e)
            return
        daftar_pasien.append(pasien)
        # hubungkan pasien dengan dokter (relasi)
        id_dokter = input("Id dokter pemeriksa (kosongkan jika belum ada): ")
        if id_dokter:
            dokter = cari_tenaga(daftar_dokter, id_dokter)
            if dokter:
                if not dokter.tambah_pasien(pasien):
                    print("Dokter nonaktif, pasien belum punya dokter.")
            else:
                print("Dokter tidak ditemukan, pasien belum punya dokter.")
        print("Pasien berhasil ditambahkan.")
    else:
        print("Kategori tidak valid.")


# ---------------- 2. TAMPILKAN DATA ----------------
def tampilkan_data():
    print("\n===== DATA DOKTER =====")
    if not daftar_dokter:
        print("(kosong)")
    for d in daftar_dokter:
        d.tampilkan_info()
        print("Pasien :", [p.nama for p in d.get_daftar_pasien()])
        print("-" * 30)

    print("\n===== DATA PERAWAT =====")
    if not daftar_perawat:
        print("(kosong)")
    for p in daftar_perawat:
        p.tampilkan_info()
        print("-" * 30)

    print("\n===== DATA PASIEN =====")
    if not daftar_pasien:
        print("(kosong)")
    for ps in daftar_pasien:
        ps.tampilkan_info()
        print("-" * 30)


# ---------------- 3. CARI DATA ----------------
def cari_data():
    print("\n--- CARI DATA ---")
    kata = input("Masukkan id atau nama: ").lower()
    ketemu = False
    for t in daftar_dokter + daftar_perawat:
        if kata in t.get_id().lower() or kata in t.nama.lower():
            t.tampilkan_info()
            print("-" * 30)
            ketemu = True
    for ps in daftar_pasien:
        if kata in ps.id_pasien.lower() or kata in ps.nama.lower():
            ps.tampilkan_info()
            print("-" * 30)
            ketemu = True
    if not ketemu:
        print("Data tidak ditemukan.")


# ---------------- 4. UBAH DATA ----------------
def ubah_data():
    print("\n--- UBAH DATA ---")
    k = pilih_kategori()
    if k == 1:
        obj = cari_tenaga(daftar_dokter, input("Masukkan id dokter: "))
    elif k == 2:
        obj = cari_tenaga(daftar_perawat, input("Masukkan id perawat: "))
    elif k == 3:
        obj = cari_pasien(input("Masukkan id pasien: "))
    else:
        print("Kategori tidak valid.")
        return
    if obj is None:
        print("Data tidak ditemukan.")
        return

    print("Data saat ini:")
    obj.tampilkan_info()
    nama = input("Nama baru: ")
    if nama:
        obj.nama = nama
    if k == 1:
        sp = input("Spesialis baru: ")
        if sp:
            obj.ubah_spesialis(sp)
    elif k == 2:
        shift = input("Shift baru: ")
        if shift:
            if not obj.ganti_shift(shift):
                print("Shift tidak valid, shift tidak diubah.")
    else:
        gejala = input("Gejala baru: ")
        if gejala:
            obj.ubah_gejala(gejala)
    print("Data berhasil diubah.")


# ---------------- 5. CEK STATUS DATA ----------------
# status tenaga medis, pemeriksaan pasien, dan ringkasan
def cek_status():
    print("\n--- CEK STATUS DATA ---")
    print("1. Aktif/nonaktifkan tenaga medis")
    print("2. Periksa pasien")
    print("3. Lihat ringkasan status")
    pilih = input_angka("Pilih: ")
    if pilih == 1:
        t = cari_tenaga(daftar_dokter + daftar_perawat, input("Id tenaga medis: "))
        if t is None:
            print("Data tidak ditemukan.")
            return
        t.ubah_status()
        print("Status sekarang:", "Aktif" if t.is_aktif() else "Nonaktif")
    elif pilih == 2:
        pasien = cari_pasien(input("Id pasien: "))
        if pasien is None:
            print("Pasien tidak ditemukan.")
            return
        dokter = pasien.get_dokter()
        if dokter is None:
            print("Pasien belum memiliki dokter.")
            return
        # dokter mengisi diagnosa, status pasien berubah jadi Sudah Diperiksa
        if dokter.periksa_pasien(pasien, input("Diagnosa dokter: ")):
            print(dokter.nama, "telah memeriksa", pasien.nama)
        else:
            print("Pemeriksaan gagal (dokter nonaktif atau diagnosa kosong).")
    elif pilih == 3:
        # hitung tenaga medis yang masih aktif
        aktif = 0
        for t in daftar_dokter + daftar_perawat:
            if t.is_aktif():
                aktif += 1
        # hitung pasien yang masih menunggu
        menunggu = 0
        for p in daftar_pasien:
            if p.get_status() == "Menunggu":
                menunggu += 1
        print("Tenaga medis aktif :", aktif)
        print("Pasien menunggu :", menunggu)
        print("Pasien selesai :", len(daftar_pasien) - menunggu)
    else:
        print("Pilihan tidak valid.")

# ---------------- 6. HAPUS DATA ----------------
def hapus_data():
    print("\n--- HAPUS DATA ---")
    k = pilih_kategori()
    if k == 1:
        daftar = daftar_dokter
        obj = cari_tenaga(daftar, input("Masukkan id dokter: "))
    elif k == 2:
        daftar = daftar_perawat
        obj = cari_tenaga(daftar, input("Masukkan id perawat: "))
    elif k == 3:
        daftar = daftar_pasien
        obj = cari_pasien(input("Masukkan id pasien: "))
    else:
        print("Kategori tidak valid.")
        return
    if obj is None:
        print("Data tidak ditemukan.")
        return

    obj.tampilkan_info()
    if input("Yakin ingin menghapus?(y/n) ").lower() !="y":
        print("Penghapusan dibatalkan.")
        return

    if k == 1:
        for p in list(obj.get_daftar_pasien()):
            obj.hapus_pasien(p)
    elif k == 3:
        dokter = obj.get_dokter()
        if dokter is not None:
            dokter.hapus_pasien(obj)

    daftar.remove(obj)
    print("Data berhasil dihapus.")


# ---------------- MENU UTAMA ----------------
# perulangan terus menampilkan menu sampai pengguna memilih keluar
def main():
    while True:
        print("\n===== APLIKASI KLINIK SEDERHANA =====")
        print("1. Tambah data")
        print("2. Tampilkan data")
        print("3. Cari data")
        print("4. Ubah data")
        print("5. Cek status data")
        print("6. Hapus data")
        print("7. Keluar dari program")
        pilihan = input("Pilih menu (1-7): ")
        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            cari_data()
        elif pilihan == "4":
            ubah_data()
        elif pilihan == "5":
            cek_status()
        elif pilihan == "6":
            hapus_data()
        elif pilihan == "7":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Menu tidak valid, coba lagi.")


# program dimulai dari sini
main()