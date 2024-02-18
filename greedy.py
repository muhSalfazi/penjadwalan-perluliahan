from prettytable import PrettyTable

class GreedyScheduler:
    def __init__(self):
        self.jadwal = {}
        self.last_class_end = {}

    def tambahMataKuliah(self, mataKuliah):
        kelas = mataKuliah['kelas']
        if kelas not in self.jadwal:
            self.jadwal[kelas] = []
            self.last_class_end[kelas] = 0

        self.jadwal[kelas].append(mataKuliah)

    def apakahWaktuTersedia(self, kelas, waktu_mulai, waktu_selesai):
        return waktu_mulai >= self.last_class_end[kelas]

    def optimalkanJadwal(self):
        jadwal_optimalkan = []

        for kelas, jadwal_kelas in self.jadwal.items():
            jadwal_kelas.sort(key=lambda x: (x['waktuMulai'], x['ruangan']))

            for mataKuliah in jadwal_kelas:
                waktu_mulai = mataKuliah['waktuMulai']
                waktu_selesai = mataKuliah['waktuSelesai']

                if self.apakahWaktuTersedia(kelas, waktu_mulai, waktu_selesai):
                    jadwal_optimalkan.append(mataKuliah)
                    self.last_class_end[kelas] = waktu_selesai

        return jadwal_optimalkan

    def tampilkanJadwal(self, jadwal_optimalkan):
        table = PrettyTable()
        table.field_names = ["Mata Kuliah", "Kelas", "Ruangan", "Waktu Mulai", "Waktu Selesai"]

        for mataKuliah in jadwal_optimalkan:
            table.add_row([mataKuliah['namaMataKuliah'], mataKuliah['kelas'], mataKuliah['ruangan'], 
                            mataKuliah['waktuMulai'], mataKuliah['waktuSelesai']])

        print(table)


# Contoh Penggunaan
scheduler = GreedyScheduler()

# Input pengguna untuk menambahkan mata kuliah
jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))


print("=================================================================")
for i in range(1, jumlah_mata_kuliah + 1):
    nama_mata_kuliah = input(f"Masukkan nama mata kuliah ke-{i}: ")
    kelas = input(f"Masukkan kelas untuk {nama_mata_kuliah}: ")
    ruangan = input(f"Masukkan ruangan untuk {nama_mata_kuliah}: ")
    waktu_mulai = int(input(f"Masukkan waktu mulai untuk {nama_mata_kuliah} (contoh: 8 untuk pukul 8:00): "))
    waktu_selesai = int(input(f"Masukkan waktu selesai untuk {nama_mata_kuliah} (contoh: 10 untuk pukul 10:00): "))
    print("=================================================================")

    # Tambahkan mata kuliah ke dalam jadwal
    scheduler.tambahMataKuliah({'namaMataKuliah': nama_mata_kuliah, 'kelas': kelas, 'ruangan': ruangan, 'waktuMulai': waktu_mulai, 'waktuSelesai': waktu_selesai})


# Optimalkan jadwal menggunakan Algoritma Greedy
jadwal_optimalkan = scheduler.optimalkanJadwal()


# Tampilkan jadwal yang sudah dioptimalkan dengan prettytable
print("Jadwal yang Dioptimalkan:")
scheduler.tampilkanJadwal(jadwal_optimalkan)
