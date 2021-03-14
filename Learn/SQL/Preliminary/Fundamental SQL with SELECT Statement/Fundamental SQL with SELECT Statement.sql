#[Perintah SELECT [2/2]](https://academy.dqlab.id/main/livecode/91/213/1086)
SELECT 
    * 
FROM 
    ms_produk;

#[Mengambil Satu Kolom dari Table](https://academy.dqlab.id/main/livecode/91/214/1093)
SELECT 
    nama_produk 
FROM 
    ms_produk;

#[Mengambil Lebih dari Satu Kolom](https://academy.dqlab.id/main/livecode/91/214/1095)
SELECT
    nama_produk, 
    harga 
FROM 
    ms_produk;

#[Membatasi Pengambilan Jumlah Row Data](https://academy.dqlab.id/main/livecode/91/214/1097)
SELECT 
    nama_produk 
FROM 
    ms_produk LIMIT 3;	

#[Menggunakan Prefix pada Nama Kolom](https://academy.dqlab.id/main/livecode/91/215/1100)
SELECT 
    ms_produk.kode_produk 
FROM 
    ms_produk;

#[Menggunakan Alias pada Kolom](https://academy.dqlab.id/main/livecode/91/215/1102)
SELECT 
    no_urut AS nomor,
    nama_produk AS nama 
FROM 
    ms_produk;

#[Menghilangkan Keyword 'AS'](https://academy.dqlab.id/main/livecode/91/215/1104)
SELECT 
    no_urut nomor,
    nama_produk nama 
FROM 
    ms_produk;

#[Menggabungkan Prefix dan Alias](https://academy.dqlab.id/main/livecode/91/215/1106)
SELECT 
    ms_produk.harga AS harga_jual 
FROM 
    ms_produk;

#[Menggunakan Alias pada Table](https://academy.dqlab.id/main/livecode/91/215/1107)
SELECT 
    * 
FROM 
    ms_produk t2;

#[Prefix dengan Alias Table](https://academy.dqlab.id/main/livecode/91/215/1108)
SELECT 
    t2.nama_produk, 
    t2.harga 
FROM 
    ms_produk t2;

#[Menggunakan WHERE](https://academy.dqlab.id/main/livecode/91/216/1111)
SELECT 
    * 
FROM 
    ms_produk 
WHERE 
    nama_produk='Tas Travel Organizer DQLab';

#[Menggunakan Operand OR](https://academy.dqlab.id/main/livecode/91/216/1112)
SELECT 
    * 
FROM 
    ms_produk 
WHERE 
    nama_produk='Gantungan Kunci DQLab' OR 
    nama_produk='Tas Travel Organizer DQLab' OR 
    nama_produk='Flashdisk DQLab 64 GB';

#[Filter untuk Angka](https://academy.dqlab.id/main/livecode/91/216/1113)
SELECT 
    * 
FROM 
    ms_produk 
WHERE 
    harga>50000;

#[Menggunakan Operand AND](https://academy.dqlab.id/main/livecode/91/216/1114)
SELECT 
    * 
FROM 
    ms_produk 
WHERE 
    nama_produk='Gantungan Kunci DQLab' AND 
    harga<50000;
