#[10 Transaksi terbesar user 12476](https://academy.dqlab.id/main/livecode/261/481/2418)
SELECT 
    seller_id, 
    buyer_id, 
    total as nilai_transaksi, 
    created_at as tanggal_transaksi
FROM 
    orders
WHERE 
    buyer_id = 12476
ORDER BY 
    3 DESC
LIMIT 
    10

#[Transaksi per bulan](https://academy.dqlab.id/main/livecode/261/481/2419)
SELECT 
	  EXTRACT(YEAR_MONTH FROM created_at) AS tahun_bulan, 
	  COUNT(1) AS jumlah_transaksi, 
	  SUM(total) AS total_nilai_transaksi
FROM 
	  orders
WHERE 
	  created_at>='2020-01-01'
GROUP BY 
	  1
ORDER BY 
	  1;

#[Pengguna dengan rata-rata transaksi terbesar di Januari 2020](https://academy.dqlab.id/main/livecode/261/481/2420)
SELECT 
	  buyer_id, 
	  COUNT(1) AS jumlah_transaksi, 
	  AVG(total) AS avg_nilai_transaksi
FROM 
	  orders
WHERE 
	  created_at>='2020-01-01' AND 
	  created_at<'2020-02-01'
GROUP BY 
	  1
HAVING 
	  COUNT(1)>= 2 
ORDER BY 
	  3 DESC
LIMIT 
	  10;

#[Transaksi besar di Desember 2019](https://academy.dqlab.id/main/livecode/261/481/2421)
SELECT
    nama_user AS nama_pembeli,
    total AS nilai_transaksi,
    created_at AS tanggal_transaksi
FROM
    orders
    INNER JOIN users ON buyer_id = user_id
WHERE
    created_at >= '2019-12-01'
    AND created_at < '2020-01-01'
    AND total >= 20000000
ORDER BY
    1;

#[Kategori Produk Terlaris di 2020](https://academy.dqlab.id/main/livecode/261/481/2422)
SELECT 
	  category, 
	  SUM(quantity) AS total_quantity, 
	  SUM(price) AS total_price
FROM 
	  orders
    INNER JOIN 
	      order_details using(order_id)
    INNER JOIN 
	      products using(product_id)
WHERE 
	  created_at>='2020-01-01'
	  AND delivery_at IS NOT NULL
GROUP BY 
	  1
ORDER BY
	  2 DESC
LIMIT 
	  5;

#[Mencari pembeli high value](https://academy.dqlab.id/main/livecode/261/482/2424)
SELECT
    nama_user AS nama_pembeli,
    COUNT(1) AS jumlah_transaksi,
    SUM(total) AS total_nilai_transaksi,
    MIN(total) AS min_nilai_transaksi
FROM
    orders
    INNER JOIN users ON buyer_id = user_id
GROUP BY
    user_id,
    nama_user
HAVING
    COUNT(1) > 5
    AND MIN(total) > 2000000
ORDER BY
    3 DESC;

#[Mencari Dropshipper](https://academy.dqlab.id/main/livecode/261/482/2425)
SELECT
	  nama_user AS nama_pembeli,
	  COUNT(1) AS jumlah_transaksi,
	  COUNT(DISTINCT orders.kodepos) AS distinct_kodepos,
	  SUM(total) AS total_nilai_transaksi,
	  AVG(total) AS avg_nilai_transaksi
FROM
	  orders
	  INNER JOIN
		    users on buyer_id = user_id
GROUP BY
	  user_id,
	  nama_user
HAVING
	  COUNT(1)>=10 AND
	  COUNT(1)=COUNT(DISTINCT orders.kodepos)
ORDER BY
	  2 DESC;

#[Pembeli sekaligus penjual](https://academy.dqlab.id/main/livecode/261/482/2427)
SELECT
    nama_user AS nama_pengguna,
    jumlah_transaksi_beli,
    jumlah_transaksi_jual
FROM
    users
    INNER JOIN (
        SELECT
            buyer_id,
            COUNT(1) AS jumlah_transaksi_beli
        FROM
            orders
        GROUP BY
            1
    ) AS buyer ON buyer_id = user_id
    INNER JOIN (
        SELECT
            seller_id,
            COUNT(1) AS jumlah_transaksi_jual
        FROM
            orders
        GROUP BY
            1
    ) AS seller ON seller_id = user_id
WHERE
    jumlah_transaksi_beli >= 7
ORDER BY
    1;				

#[Lama transaksi dibayar](https://academy.dqlab.id/main/livecode/261/482/2428)
SELECT
    EXTRACT(
        YEAR_MONTH
        FROM
            created_at
    ) AS tahun_bulan,
    COUNT(1) AS jumlah_transaksi,
    AVG(DATEDIFF(paid_at, created_at)) AS avg_lama_dibayar,
    MIN(DATEDIFF(paid_at, created_at)) min_lama_dibayar,
    MAX(DATEDIFF(paid_at, created_at)) max_lama_dibayar
FROM
    orders
WHERE
    paid_at IS NOT NULL
GROUP BY
    1
ORDER BY
    1;
