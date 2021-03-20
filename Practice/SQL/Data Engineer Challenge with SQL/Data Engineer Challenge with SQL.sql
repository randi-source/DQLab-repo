#[Produk DQLab Mart](https://academy.dqlab.id/main/projectcode/99/195/946)
SELECT 
    no_urut, 
    kode_produk, 
    nama_produk, 
    harga 
FROM 
    ms_produk 
WHERE 
    harga>=50000 AND 
    harga<=150000

#[Thumb drive di DQLab Mart](https://academy.dqlab.id/main/projectcode/99/195/947)
SELECT 
    * 
FROM 
    ms_produk
WHERE 
    nama_produk LIKE '%Flashdisk%';

#[Pelanggan Bergelar](https://academy.dqlab.id/main/projectcode/99/195/948)
SELECT 
    * 
FROM 
    ms_pelanggan
WHERE 
    nama_pelanggan LIKE '%S.H%' OR 
    nama_pelanggan LIKE '%Ir.%'OR 
    nama_pelanggan LIKE '%Drs.%'

#[Mengurutkan Nama Pelanggan](https://academy.dqlab.id/main/projectcode/99/195/949)
SELECT 
    nama_pelanggan 
FROM 
    ms_pelanggan 
ORDER BY 
    nama_pelanggan ASC;

#[Mengurutkan Nama Pelanggan Tanpa Gelar](https://academy.dqlab.id/main/projectcode/99/195/950)
SELECT 
    nama_pelanggan 
FROM 
    ms_pelanggan 
ORDER BY 
    REPLACE(nama_pelanggan,'Ir. ','') ASC;

#[Nama Pelanggan yang Paling Panjang](https://academy.dqlab.id/main/projectcode/99/195/951)
SELECT 
    nama_pelanggan
FROM 
    ms_pelanggan 
WHERE 
    LENGTH(nama_pelanggan)= (
    SELECT 
        MAX(LENGTH(nama_pelanggan))
    FROM 
        ms_pelanggan);

#[Nama Pelanggan yang Paling Panjang dengan Gelar](https://academy.dqlab.id/main/projectcode/99/195/952)
SELECT
	  nama_pelanggan
FROM
	  ms_pelanggan
WHERE
	  LENGTH(nama_pelanggan) IN(
	  (SELECT
	  	  MAX(LENGTH(nama_pelanggan))
	  FROM 
        ms_pelanggan
	   ),
	  (SELECT
	      MIN(LENGTH(nama_pelanggan))
	   FROM
	      ms_pelanggan
	   ))
ORDER BY
	LENGTH(nama_pelanggan) DESC;

#[Kuantitas Produk yang Banyak Terjual](https://academy.dqlab.id/main/projectcode/99/195/953)
SELECT
	  ms_produk.kode_produk,
	  nama_produk,
	  SUM(qty) AS total_qty
FROM
	  ms_produk
INNER JOIN 
    tr_penjualan_detail
ON
	  ms_produk.kode_produk=tr_penjualan_detail.kode_produk
GROUP BY
	  kode_produk,
	  nama_produk
HAVING
	  SUM(qty) > 2;

#[Pelanggan Paling Tinggi Nilai Belanjanya](https://academy.dqlab.id/main/projectcode/99/195/954)
SELECT
	  tr_penjualan.kode_pelanggan,
	  ms_pelanggan.nama_pelanggan,
	  SUM(tr_penjualan_detail.qty*tr_penjualan_detail.harga_satuan)  AS total_harga
FROM
	  ms_pelanggan
INNER JOIN 
    tr_penjualan 
USING 
    (kode_pelanggan)
INNER JOIN 
    tr_penjualan_detail 
USING 
    (kode_transaksi)

GROUP BY
	  kode_pelanggan,
	  nama_pelanggan
ORDER BY
	  total_harga DESC
LIMIT
	  1;

#[Pelanggan yang Belum Pernah Berbelanja](https://academy.dqlab.id/main/projectcode/99/195/955)
SELECT
	  kode_pelanggan,
	  nama_pelanggan,
	  alamat
FROM
	  ms_pelanggan
WHERE
	  kode_pelanggan NOT IN(
	  SELECT
	  	  kode_pelanggan
	  FROM
	  	  tr_penjualan);

#[Transaksi Belanja dengan Daftar Belanja lebih dari 1](https://academy.dqlab.id/main/projectcode/99/195/956)
SELECT
	  tp.kode_transaksi,
	  tp.kode_pelanggan,
	  mp.nama_pelanggan,
	  tp.tanggal_transaksi,
	  COUNT(tpd.qty) AS jumlah_detail
FROM
	  ms_pelanggan mp
INNER JOIN 
    tr_penjualan tp 
USING 
    (kode_pelanggan)
INNER JOIN 
    tr_penjualan_detail tpd 
USING 
    (kode_transaksi)
GROUP BY
	  tp.kode_transaksi,
	  tp.kode_pelanggan,
	  mp.nama_pelanggan,
	  tp.tanggal_transaksi
HAVING 
    jumlah_detail > 1;
