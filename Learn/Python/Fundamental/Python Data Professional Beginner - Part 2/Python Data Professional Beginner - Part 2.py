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

#[Tugas Praktek](https://academy.dqlab.id/main/livecode/160/298/1344)
# Dua buah data yang tersimpan dalam tipe list
data1 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]
# Fungsi rata-rata data
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rata_rata = jumlah/len(data)
    return rata_rata
# Definisikan fungsi hitung_standar_deviasi
def hitung_standar_deviasi(data):
    rata_rata_data = hitung_rata_rata(data)
    varians = 0
    for item in data:
        varians += (item - rata_rata_data) ** 2
        varians /= len(data)
    standar_deviasi = varians ** (1/2)
    return standar_deviasi
# Hitung nilai standar deviasi dari kedua data yang dimiliki
print('Standar deviasi data1:')
print(hitung_standar_deviasi(data1))
print('Standar deviasi data2:')
print(hitung_standar_deviasi(data2))

#[Tugas Praktek](https://academy.dqlab.id/main/livecode/160/298/1345)
# Data properti
tabel_properti = {
'luas_tanah': [70, 70, 70, 100, 100, 100, 120, 120, 150, 150],
'luas_bangunan': [50, 60, 60, 50, 70, 70, 100, 80, 100, 90],
'jarak': [15, 30, 55, 30, 25, 50, 20, 50, 50, 15],
'harga': [500, 400, 300, 700, 1000, 650, 2000, 1200, 1800, 3000]
}
# Fungsi rata-rata data
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item
        rata_rata = jumlah/len(data)
        return rata_rata
# Fungsi hitung_standar_deviasi
def hitung_standar_deviasi(data):
    rata_rata_data = hitung_rata_rata(data)
    varians = 0
    for item in data:
        varians += (item - rata_rata_data) ** 2
        varians /= len(data)
        standar_deviasi = varians ** (1/2)
        return standar_deviasi
# Definisikan fungsi untuk menghitung rata-rata dan standar deviasi
# setiap kolom pada tabel_properti yang diberikan oleh key dict.
def deskripsi_properti(tabel):
	for key in tabel.keys():
		print('Rata-rata ' + key + ':')
		print(hitung_rata_rata(tabel[key]))
		print('Standar deviasi ' + key + ':')
		print(hitung_standar_deviasi(tabel[key]))
		print('')
# Panggil fungsi deskripsi_properti untuk menghitung rata-rata
# dan standar deviasi setiap kolom pada tabel_properti
deskripsi_properti(tabel_properti)

#[Membaca Berkas Teks – Part 1](https://academy.dqlab.id/main/livecode/160/299/1381)
# Membaca file hello.txt dengan fungsi read()
print(">>> Membaca file hello.txt dengan fungsi read()")
file = open("hello.txt", "r")
content = file.read()
file.close()
print(content)
# Membaca file hello.txt dengan fungsi readline()
print(">>> Membaca file hello.txt dengan fungsi readline()")
file = open("hello.txt", "r")
first_line = file.readline()
second_line = file.readline()
file.close()
print(first_line)
print(second_line)

#[Membaca Berkas Teks – Part 2](https://academy.dqlab.id/main/livecode/160/299/1382)
# Membaca file hello.txt dengan fungsi readlines()
print(">>> Membaca file hello.txt dengan fungsi readlines()")
file = open("hello.txt", "r")
all_lines = file.readlines()
file.close()
print(all_lines)
# Membaca file hello.txt dengan menerapkan looping
print(">>> Membaca file hello.txt dengan menerapkan looping")
file = open("hello.txt", "r")
for line in file:
    print(line)

#Menulis Berkas Teks – Part 1[](https://academy.dqlab.id/main/livecode/160/299/1383)
# Menulis ke file hello_write.txt
file = open("hello.txt", "w")
file.write("Sekarang kita belajar menulis dengan menggunakan Python")
file.write("Menulis konten file dengan mode w (write).")
file.close()

#[Menulis Berkas Teks – Part 2](https://academy.dqlab.id/main/livecode/160/299/1384)
# Menulis ke file dengan mode append
file = open("hello.txt", "a")
file.writelines([
"Sekarang kita belajar menulis dengan menggunakan Python", 
"Menulis konten file dengan mode a (append)."
])
file.close()

#[Fungsi dalam Library Matematika – Part 1](https://academy.dqlab.id/main/livecode/160/299/1388)
# Import library math
import math
# Fungsi math.ceil()
print(">>> Fungsi math.ceil()")
x = 10.32
y = 13.87
x_ceil = math.ceil(x)
y_ceil = math.ceil(y)
print(x_ceil)
print(y_ceil)
# Fungsi math.floor()
print(">>> Fungsi math.floor()")
x_floor = math.floor(x)
y_floor = math.floor(y)
print(x_floor)
print(y_floor)
# Fungsi math.fabs()
print(">>> Fungsi math.fabs()")
x = 10.32
y = -13.87
x = math.fabs(x)
y = math.fabs(y)
print(x)
print(y)
# Fungsi math.factorial()
print(">>> Fungsi math.factorial()")
x_factorial = math.factorial(5)
print(x_factorial)
# Fungsi math.fsum()
print(">>> Fungsi math.fsum()")
x = [1, 2, 3, 4, 5, 6, -6, -5, -4]
total = math.fsum(x)
print(total)

#[Fungsi dalam Library Matematika – Part 2](https://academy.dqlab.id/main/livecode/160/299/1389)
# Import library math
import math
# Fungsi math.log()
print(">>> Fungsi math.log()")
# x = log basis 2 dari 8
x = math.log(8, 2)
# y = log basis 3 dari 81
y = math.log(81, 3)
# z = log basis 10 dari 10000
z = math.log(10000,10)
print(x)
print(y)
print(z)
# Fungsi math.sqrt()
print(">>> Fungsi math.sqrt()")
# akar kuadrat dari 100
x = math.sqrt(100)
print(x)
# akar kuadrat dari 2
y = math.sqrt(2)
print(y)
# Fungsi math.copysign()
print(">>> Fungsi math.copysign()")
x = 10.32
y = -13.87
z = -15
x = math.copysign(x, z)
y = math.copysign(y, z)
z = math.copysign(z, 10)
print(x)
print(y)
print(z)

#[Harga Rumah di Tangerang](https://academy.dqlab.id/main/livecode/160/303/1392)
# STEP 1:
# Baca file "harga_rumah.txt"
file_harga_rumah = open("harga_rumah.txt", "r")
data_harga_rumah = file_harga_rumah.readlines()
file_harga_rumah.close()
# Buat list of dict dengan nama harga rumah
key_harga_rumah = data_harga_rumah[0].replace("\n","").split(",")
harga_rumah = []
for baris in data_harga_rumah[1:]:
    baris_harga_rumah = baris.replace("\n","").split(",")
dict_harga_rumah = dict()
for i in range(len(baris_harga_rumah)):
    dict_harga_rumah[key_harga_rumah[i]] = baris_harga_rumah[i]
harga_rumah.append(dict_harga_rumah)
print(harga_rumah)
# STEP 2:
# Buat fungsi get_all_specified_attribute yang menerima parameter list_of_dictionary
# (tipe data list yang berisikan sekumpulan tipe data dictionary) dan specified_key
# (tipe data string). Fungsi akan mengembalikan sebuah list yang berisikan seluruh
# atribut dengan kunci (key) specified_key.
def get_all_specified_attributes(list_of_dictionary, specified_key):
    list_attributes = []
    for data in list_of_dictionary:
        attribute = data[specified_key]
        list_attributes.append(attribute)
    return list_attributes
# STEP 3:
# Buat fungsi fungsi min_value yang menerima parameter list_attributes (berupa
# tipe data list) dan mengembalikan nilai terkecil dalam list_attributes
def min_value(list_attributes):
    min_attribute = 9999
    for attr in list_attributes:
        if int(attr) < min_attribute:
            min_attribute = int(attr)
    return min_attribute
# Buat fungsi dan max_value yang menerima parameter list_attribute dan
# mengembalikan nilai terbesar dalam list_attributes.
def max_value(list_attributes):
    max_attribute = -9999
    for attr in list_attributes:
        if int(attr) > max_attribute:
            max_attribute = int(attr)
    return max_attribute
# STEP 4:
# Buat fungsi transform_attribute yang menerima parameter attr (sebuah
# bilangan), max_attr (sebuah bilangan) dan min_attr (sebuah bilangan)
# yang mengembalikan nilai transformasi dari sebuah attribute.
def transform_attribute(attr, max_attr, min_attr):
    nilai_transformasi = (attr - min_attr) / (max_attr - min_attr)
    return nilai_transformasi
# STEP 5:
# Buat fungsi data_transformation yang menerima parameter list_of_dictionary
# (sebuah list yang berisikan tipe data dictionary) dan list_attribute_names
# (sebuah list yang berisikan tipe data string) mengembalikan hasil
# transformasi data dari list_of_dictionary berdasarkan list_attribute_names
# dan attr_info telah dispesifikasikan.
def data_transformation(list_of_dictionary, list_attribute_names):
    attr_info = {}
    for attr_name in list_attribute_names:
        specified_attributes = get_all_specified_attributes(list_of_dictionary, attr_name)
        max_attr = max_value(specified_attributes)
        min_attr = min_value(specified_attributes)
        attr_info[attr_name] = {'max': max_attr, 'min': min_attr}
        data_idx = 0
        while(data_idx < len(list_of_dictionary)):
            list_of_dictionary[data_idx][attr_name] = transform_attribute(int(list_of_dictionary[data_idx][attr_name]), max_attr, min_attr)
            data_idx += 1
    return list_of_dictionary, attr_info
# STEP 6:
# Berdasarkan data baru dan attr_info ini, buat fungsi transform_data yang
# menerima parameter data dan attr_info dan mengembalikan nilai atribut
# dari data baru yang telah ditransformasikan.
def transform_data(data, attr_info):
    for key_name in data.keys():
        data[key_name] = (data[key_name] - attr_info[key_name]['min']) / (
attr_info[key_name]['max'] - attr_info[key_name]['min'])
    return data
# STEP 7:
# Buat fungsi yang digunakan untuk sistem prediksi harga berdasarkan
# nilai kemiripan atribut!
def abs_value(value):
    if value < 0:
        return -value
    else:
        return value
def price_based_on_similarity(data, list_of_data):
    prediksi_harga = 0
    perbedaan_terkecil = 999
    for data_point in list_of_data:
        perbedaan= abs_value(data['tanah'] - data_point['tanah'])
        perbedaan+= abs_value(data['bangunan'] - data_point['bangunan'])
        perbedaan+= abs_value(data['jarak_ke_pusat'] - data_point['jarak_ke_pusat'])
        if perbedaan < perbedaan_terkecil:
            prediksi_harga = data_point['harga']
            perbedaan_terkecil = perbedaan
    return prediksi_harga
# STEP 8:
# Hitung harga rumah yang telah ditransformasikan ke dalam variabel
# harga_rumah berikut dengan atributnya attr_info
harga_rumah, attr_info = data_transformation(harga_rumah,
['tanah','bangunan','jarak_ke_pusat'])
# Gunakan variabel data untuk memprediksi harga rumah
data = {'tanah': 110, 'bangunan': 80, 'jarak_ke_pusat': 35}
# Transformasikan data tersebut dengan dengan menggunakan attr_info yang telah
# diperoleh yang kembali disimpan ke variabel data.
data = transform_data(data, attr_info)
# Hitunglah prediksi harga dari variabel data tersebut.
harga = price_based_on_similarity(data, harga_rumah)
print("Prediksi harga rumah: ", harga)
