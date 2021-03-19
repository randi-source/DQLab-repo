#[Tugas Praktek](https://academy.dqlab.id/main/livecode/244/406/2034)
SELECT 
    * 
FROM 
    ms_item_kategori;

SELECT 
    * 
FROM 
    ms_item_warna;

#[Menggabungkan Tabel dengan Key Columns](https://academy.dqlab.id/main/livecode/244/406/2038)
SELECT 
    * 
FROM 
    ms_item_kategori, 
    ms_item_warna
WHERE 
    nama_barang = nama_item;

#[Bagaimana jika urutan Tabel diubah?](https://academy.dqlab.id/main/livecode/244/406/2044)
SELECT 
    * 
FROM 
    ms_item_warna, 
    ms_item_kategori
WHERE 
    nama_barang=nama_item;

#[Menggunakan Prefix Nama Tabel](https://academy.dqlab.id/main/livecode/244/406/2045)
SELECT 
    ms_item_kategori.*, 
    ms_item_warna.*
FROM 
    ms_item_warna,  
    ms_item_kategori
WHERE 
    nama_barang=nama_item;

#[Penggabungan Tanpa Kondisi](https://academy.dqlab.id/main/livecode/244/406/2046)
SELECT 
    * 
FROM 
    ms_item_kategori, 
    ms_item_warna;

#[Tugas Praktek: Menggunakan INNER JOIN (1/3)](https://academy.dqlab.id/main/livecode/244/407/2051)
SELECT 
    *
FROM 
    ms_item_warna
INNER JOIN 
    ms_item_kategori
ON 
    ms_item_warna.nama_barang = ms_item_kategori.nama_item;

#[tabel tr_penjualan dan tabel ms_produk](https://academy.dqlab.id/main/livecode/244/407/2052)
SELECT 
    * 
FROM 
    tr_penjualan;
SELECT 
    * 
FROM 
    ms_produk;

#[Tugas Praktek: Menggunakan INNER JOIN (2/3)](https://academy.dqlab.id/main/livecode/244/407/2054)
SELECT 
    * 
FROM 
    tr_penjualan
INNER JOIN 
    ms_produk
ON 
    tr_penjualan.kode_produk=ms_produk.kode_produk;

#[Tugas Praktek: Menggunakan INNER JOIN (3/3)](https://academy.dqlab.id/main/livecode/244/407/2057)
SELECT 
    tr_penjualan.kode_transaksi, 
    tr_penjualan.kode_pelanggan, 
    tr_penjualan.kode_produk, 
    ms_produk.nama_produk, 
    ms_produk.harga, 
    tr_penjualan.qty, 
    ms_produk.harga*tr_penjualan.qty AS total
FROM 
    tr_penjualan
INNER JOIN 
    ms_produk
ON 
    tr_penjualan.kode_produk=ms_produk.kode_produk;

#[Tabel yang Akan Digabungkan](https://academy.dqlab.id/main/livecode/244/408/2061)
SELECT 
    * 
FROM 
    tabel_A;
SELECT 
    * 
FROM 
    tabel_B;

#[Menggunakan UNION](https://academy.dqlab.id/main/livecode/244/408/2062)
SELECT 
    * 
FROM 
    tabel_A
UNION
SELECT 
    * 
FROM 
    tabel_B;

#[Menggunakan UNION dengan Klausa WHERE](https://academy.dqlab.id/main/livecode/244/408/2063)
SELECT 
    * 
FROM 
    tabel_A
WHERE 
    kode_pelanggan='dqlabcust03'
UNION
SELECT 
    * 
FROM 
    tabel_B
WHERE 
    kode_pelanggan='dqlabcust03';

#[Menggunakan UNION dan Menyelaraskan Kolom-Kolomnya.](https://academy.dqlab.id/main/livecode/244/408/2065)
SELECT 
    CustomerName, 
    ContactName, 
    City, 
    PostalCode
FROM 
    Customers
UNION
SELECT 
    SupplierName, 
    ContactName, 
    City, 
    PostalCode
FROM 
    Suppliers;

#[Project INNER JOIN](https://academy.dqlab.id/main/livecode/244/409/2070)
SELECT DISTINCT 
    ms_pelanggan.kode_pelanggan, 
    ms_pelanggan.nama_customer, 
    ms_pelanggan.alamat
FROM 
    ms_pelanggan
INNER JOIN 
    tr_penjualan
ON 
    ms_pelanggan.kode_pelanggan=tr_penjualan.kode_pelanggan
WHERE 
    tr_penjualan.nama_produk='Kotak Pensil DQLab' OR 
    tr_penjualan.nama_produk='Flashdisk DQLab 32 GB' OR 
    tr_penjualan.nama_produk='Sticky Notes DQLab 500 sheets';

#[Project UNION](https://academy.dqlab.id/main/livecode/244/409/2071)
SELECT 
    nama_produk, 
    kode_produk, 
    harga
FROM 
    ms_produk_1
WHERE 
    harga < 100000
UNION
SELECT 
    nama_produk, 
    kode_produk, 
    harga
FROM 
    ms_produk_2
WHERE 
    harga <50000;
