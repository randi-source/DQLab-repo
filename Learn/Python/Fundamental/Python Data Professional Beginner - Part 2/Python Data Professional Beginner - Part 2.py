#[Tugas Praktek](https://academy.dqlab.id/main/livecode/160/296/1328)
# Data keuangan
keuangan = {
'pengeluaran': [2, 2.5, 2.25, 2.5, 3.2, 2.5, 3.5, 4, 3],
'pemasukan': [7.8, 7.5, 9, 7.6, 7.2, 7.5, 7, 10, 7.5]
}
# Perhitungan rata-rata pemasukan dan rata-rata pengeluaran
total_pengeluaran = 0
total_pemasukan = 0
for biaya in keuangan['pengeluaran']: 
    total_pengeluaran += biaya
for biaya in keuangan['pemasukan']: 
    total_pemasukan += biaya
rata_rata_pengeluaran = total_pengeluaran/len(keuangan['pengeluaran'])
rata_rata_pemasukan = total_pemasukan/len(keuangan['pemasukan'])
print(rata_rata_pengeluaran) 
print(rata_rata_pemasukan)

#[Apa itu String Manipulation?](https://academy.dqlab.id/main/livecode/160/297/1330)
nama_produk = "Sepatu Niko"
nama_produk = nama_produk[:2]+"P"+nama_produk[3:9]+"K"+nama_produk[-1]
print(nama_produk)
print(nama_produk[:7])
print(nama_produk[7:])
print(len(nama_produk))

#[Operator “+” untuk Tipe Data String](https://academy.dqlab.id/main/livecode/160/297/1331)
nama_depan = 'John'
nama_belakang = 'Doee'
nama_lengkap = nama_depan+' '+nama_belakang
print(nama_lengkap)
umur = '27 tahun'
alamat = 'Jl. Anggrek No. 100'
nama_umur_alamat = 'Hi, saya ' + nama_lengkap + ' umur ' + umur + ', tinggal di ' + alamat + '.'
print(nama_umur_alamat)

#[Menghilangkan Spasi di Awal dan/atau di Akhir](https://academy.dqlab.id/main/livecode/160/297/1332)
# Fitur .strip()
print(">>> Fitur .strip()")
kata_sambutan = ' halo, selamat siang!   '
kata_sambutan = kata_sambutan.strip()
print(kata_sambutan)
# Fitur .lstrip()
print(">>> Fitur .lstrip()")
kata_sambutan = ' halo, selamat siang!   '
kata_sambutan = kata_sambutan.lstrip()
print(kata_sambutan)
# Fitur .rstrip()
print(">>> Fitur .rstrip()")
kata_sambutan = ' halo, selamat siang!   '
kata_sambutan = kata_sambutan.rstrip()
print(kata_sambutan)

#[Pemecahan, Penggabungan, dan Penggantian String](https://academy.dqlab.id/main/livecode/160/297/1334)
# Fitur .split()
print(">>> Fitur .split()")
bilangan = "ani dan budi dan wati dan johan"
karakter = bilangan.split("dan")
print(karakter)
kata = bilangan.split(" ")
print(kata)
# Fitur .join()
print(">>> Fitur .join()")
pemisah = " dan "
karakter = ["Ricky", "Peter", "Jordan"]
kalimat = pemisah.join(karakter)
print(kalimat)
# Fitur .replace()
print(">>> Fitur .replace()")
kalimat = "apel malang apel yang paling segar, apel sehat, apel nikmat"
kalimat = kalimat.replace("apel", "jeruk")
print(kalimat)

#[Menentukan Posisi dan Jumlah Sub-string pada String](https://academy.dqlab.id/main/livecode/160/297/1335)
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
# Fitur .find()
print(">>> Fitur .find()")
print(teks.find("Apel"))
print(teks.find("malang"))
# Fitur .count()
print(">>> Fitur .count()")
kemunculan_kata_apel = teks.count("apel")
print(kemunculan_kata_apel)

#[Menentukan String Apakah Diawali/Diakhiri oleh Sub-string](https://academy.dqlab.id/main/livecode/160/297/1336)
# Fitur .startswith()
print(">>> Fitur .startswith()")
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
print(teks.startswith("Apel"))
print(teks.startswith("apel"))
# Fitur .endswith()
print(">>> Fitur .endswith()")
print(teks.endswith("lainnya"))
print(teks.endswith("apel"))

#[Tugas Praktek](https://academy.dqlab.id/main/livecode/160/297/1337)
judul_artikel = [
"Buah Salak Baik untuk Mata", "Buah Salak Kaya Potasium", 
"Buah Jeruk Kaya Vitamin C", "Buah Salak Kaya Manfaat", 
"Salak Baik untuk Jantung", "Jeruk dapat Memperkuat Tulang", 
"Jeruk Mencegah Penyakit Asma", "Jeruk Memperkuat Gigi", 
"Jeruk Mencegah Kolesterol Jahat", "Salak Mencegah Diabetes", 
"Salak Memperkuat Dinding Usus", "Salak Baik untuk Darah",
"Jeruk Kaya Manfaat untuk Jantung", "Salak si Kecil yang Baik", 
"Jeruk dan Salak Buah Kaya Manfaat", "Buah Jeruk Enak",
"Tips Panen Jeruk Ribuan Kilo", "Tips Bertanam Salak", 
"Salak Manis untuk Berbuka", "Jeruk Baik untuk Wajah"
]
jumlah_artikel_jeruk = 0
jumlah_artikel_salak = 0
for judul in judul_artikel:
    if judul.count("Jeruk") > 0: 
        jumlah_artikel_jeruk += 1
    if judul.count("Salak") > 0:
        jumlah_artikel_salak += 1
print(jumlah_artikel_jeruk) 
print(jumlah_artikel_salak)

#[Tugas Praktek](https://academy.dqlab.id/main/livecode/160/297/1338)
judul_artikel = [
"Buah Salak Baik untuk Mata", "Buah Salak Kaya Potasium", 
"Buah Jeruk Kaya Vitamin C", "Buah Salak Kaya Manfaat", 
"Salak Baik untuk Jantung", "Jeruk dapat Memperkuat Tulang", 
"Jeruk Mencegah Penyakit Asma", "Jeruk Memperkuat Gigi", 
"Jeruk Mencegah Kolesterol Jahat", "Salak Mencegah Diabetes", 
"Salak Memperkuat Dinding Usus", "Salak Baik untuk Darah",
"Jeruk Kaya Manfaat untuk Jantung", "Salak si Kecil yang Baik", 
"Jeruk dan Salak Buah Kaya Manfaat", "Buah Jeruk Enak",
"Tips Panen Jeruk Ribuan Kilo", "Tips Bertanam Salak", 
"Salak Manis untuk Berbuka", "Jeruk Baik untuk Wajah"
]
kata_positif = ["Kaya", "Baik", "Mencegah", "Memperkuat"]
kata_positif_jeruk = 0
kata_positif_salak = 0
for judul in judul_artikel:
	for kata in kata_positif:
		if judul.count("Jeruk") > 0 and judul.count(kata) > 0:
			kata_positif_jeruk += 1
		if judul.count("Salak") > 0 and judul.count(kata) > 0:
			kata_positif_salak += 1
print(kata_positif_jeruk)
print(kata_positif_salak)

#[Fungsi Pertama](https://academy.dqlab.id/main/livecode/160/298/1340)
# Definisikan fungsi
def contoh_fungsi():
    print("Halo Dunia")
    print("Aku sedang belajar bahasa Python")
# Panggil fungsi yang telah didefinisikan
contoh_fungsi()

#[Fungsi Kedua](https://academy.dqlab.id/main/livecode/160/298/1341)
# Definsikan fungsi 
def fungsi_dengan_argumen(nama_depan, nama_belakang):
    print(nama_depan+ " " +nama_belakang)
# Panggil fungsi dengan memasukkan argumen
# nama_depan yaitu "John" dan nama_belakang "Doe"
fungsi_dengan_argumen("John", "Doe")

#[Fungsi Ketiga](https://academy.dqlab.id/main/livecode/160/298/1342)
# Definsikan fungsi dengan nilai default argument kedua adalah "".
def fungsi_dengan_argumen(nama_depan, nama_belakang=""):
	print(nama_depan+ " " +nama_belakang)
# Panggil fungsi dengan memasukkan argumen nama_depan "John"
fungsi_dengan_argumen("John")
# Panggil fungsi dengan memasukkan argumen
# nama_depan yaitu "John" dan nama_belakang "Doe"
fungsi_dengan_argumen("John", "Doe")

#[Tugas Praktek](https://academy.dqlab.id/main/livecode/160/298/1343)
# Dua buah data yang tersimpan dalam tipe list
data1 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]
# Definisikan fungsi hitng_rata_rata
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rata_rata = jumlah/len(data)
    return rata_rata
# Hitung nilai rata-rata dari kedua data yang dimiliki
print('Rata-rata data1:')
print(hitung_rata_rata(data1))
print('Rata-rata data2:')
print(hitung_rata_rata(data2))

#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()
