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


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()
