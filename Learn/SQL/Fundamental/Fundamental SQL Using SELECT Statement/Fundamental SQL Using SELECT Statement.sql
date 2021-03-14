#[Mengambil Seluruh Kolom dalam suatu Tabel](https://academy.dqlab.id/main/livecode/213/385/1898)
SELECT 
    * 
FROM 
    ms_produk;				

#[Mengambil Satu Kolom dari Tabel](https://academy.dqlab.id/main/livecode/213/385/1899)
SELECT 
    nama_produk 
FROM 
    ms_produk;

#[Mengambil Lebih dari Satu Kolom dari Tabel](https://academy.dqlab.id/main/livecode/213/385/1901)
SELECT 
    nama_produk, 
    harga 
FROM 
    ms_produk;

#[Membatasi Pengambilan Jumlah Row Data](https://academy.dqlab.id/main/livecode/213/385/1903)
SELECT 
    nama_produk, 
    harga 
FROM 
    ms_produk 
LIMIT 
    5;

#[Penggunaan SELECT DISTINCT statement](https://academy.dqlab.id/main/livecode/213/385/1988)
SELECT DISTINCT 
  nama_customer, 
  alamat 
FROM 
  ms_pelanggan;

#[Menggunakan Prefix pada Nama Kolom](https://academy.dqlab.id/main/livecode/213/386/1907)
SELECT 
    ms_produk.kode_produk 
FROM 
    ms_produk;

#[Menggunakan Alias pada Kolom](https://academy.dqlab.id/main/livecode/213/386/1909)
SELECT 
    no_urut AS nomor, 
    nama_produk AS nama 
FROM 
    ms_produk;

#[Menghilangkan Keyword 'AS'](https://academy.dqlab.id/main/livecode/213/386/1911)
SELECT 
    no_urut nomor, 
    nama_produk nama 
FROM 
    ms_produk;

#[Menggabungkan Prefix dan Alias](https://academy.dqlab.id/main/livecode/213/386/1913)
SELECT 
    ms_produk.harga AS harga_jual 
FROM 
    ms_produk;

#[Menggunakan Alias pada Tabel](https://academy.dqlab.id/main/livecode/213/386/1914)
SELECT 
    * 
FROM 
    ms_produk t2;	

#[Prefix dengan Alias Tabel](https://academy.dqlab.id/main/livecode/213/386/1915)
SELECT 
    t2.nama_produk, 
    t2.harga 
FROM 
    ms_produk t2;

#[Menggunakan WHERE](https://academy.dqlab.id/main/livecode/213/387/1919)
SELECT 
    * 
FROM 
    ms_produk 
WHERE 
    nama_produk='Tas Travel Organizer DQLab';

#[Menggunakan Operand OR](https://academy.dqlab.id/main/livecode/213/387/1920)
SELECT 
    * 
FROM 
    ms_produk 
WHERE 
    nama_produk='Gantungan Kunci DQLab' OR 
    nama_produk='Tas Travel Organizer DQLab' OR 
    nama_produk='Flashdisk DQLab 64 GB';

#[Filter untuk Angka](https://academy.dqlab.id/main/livecode/213/387/1921)
SELECT 
    * 
FROM 
    ms_produk 
WHERE 
    harga > 50000;

#[Menggunakan Operand AND](https://academy.dqlab.id/main/livecode/213/387/1924)
SELECT 
    * 
FROM 
    ms_produk 
WHERE 
    nama_produk='Gantungan Kunci DQLab' AND 
    harga <50000;	

#[Proyek dari Cabang A](https://academy.dqlab.id/main/livecode/213/388/1929)
SELECT 
    kode_pelanggan, 
    nama_produk, 
    qty, 
    harga, 
    qty*harga AS total 
FROM 
    tr_penjualan 
WHERE 
    qty*harga >= 100000 
ORDER BY 
    total DESC; 
