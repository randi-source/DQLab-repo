#[Memahami table](https://academy.dqlab.id/main/projectcode/246/418/2102)
SELECT 
    * 
FROM 
    orders_1 
limit 
    5;

SELECT 
    * 
FROM 
    orders_2 
limit 
    5;
    
SELECT 
    * 
FROM 
    customer 
limit 
    5;

#[Total Penjualan dan Revenue pada Quarter-1 (Jan, Feb, Mar) dan Quarter-2 (Apr,Mei,Jun)](https://academy.dqlab.id/main/projectcode/246/420/2103)
SELECT 
	  SUM(quantity) AS total_penjualan, 
	  SUM(quantity*priceEach) AS revenue
FROM
	  orders_1
WHERE
	  status='Shipped';

SELECT 
	  SUM(quantity) AS total_penjualan, 
	  SUM(quantity * priceEach) AS revenue
FROM
	  orders_2
WHERE
	  status='Shipped';

#[Menghitung persentasi keseluruhan penjualan](https://academy.dqlab.id/main/projectcode/246/420/2104)
SELECT
	  quarter,
	  SUM(quantity) AS total_penjualan,
	  SUM(quantity*priceEach) AS revenue
FROM (
	  SELECT 
		    orderNumber, 
		    status, 
		    quantity, 
		    priceEach,
		    "1" AS quarter
	  FROM 
		    orders_1
	  UNION
	  SELECT 
		    orderNumber, 
		    status, 
		    quantity, 
		    priceEach,
		    "2" AS quarter
	  FROM 
		    orders_2
    )AS table_a

WHERE
	  status='Shipped'
GROUP BY
	  quarter;

#[Apakah jumlah customers xyz.com semakin bertambah?](https://academy.dqlab.id/main/projectcode/246/421/2106)
SELECT 
	  quarter,
	  COUNT(DISTINCT customerID) AS total_customers
FROM
	  (
	  SELECT
	 	    customerID, 
	 	    createDate,
	 	    QUARTER(createDate) AS quarter
	  FROM 
	 	    customer
	  WHERE 
 		    createDate BETWEEN "2004-01-01" AND "2004-06-30"
	 ) AS tabel_b
GROUP BY
	quarter;

#[Seberapa banyak customers tersebut yang sudah melakukan transaksi?](https://academy.dqlab.id/main/projectcode/246/421/2107)
SELECT
	  quarter,
	  COUNT(DISTINCT customerID) AS total_customers
FROM
	  (
	  SELECT
	  	  customerID,
	  	  createDate,
	  	  QUARTER(createDate) AS quarter
	  FROM
	  	  customer
	  WHERE
	  	  createDate BETWEEN '2004-01-01'
	  	  AND '2004-06-30'
	  ) AS tabel_b
WHERE
	  customerID
	  IN(
		    SELECT DISTINCT 
            customerID
		    FROM 
            orders_1 
		    UNION
		    SELECT DISTINCT 
            customerID
		    FROM 
            orders_2
	     )
GROUP BY
	  quarter;
	  
#[Category produk apa saja yang paling banyak di-order oleh customers di Quarter-2?](https://academy.dqlab.id/main/projectcode/246/421/2108)
SELECT *
FROM (
	  SELECT
		    categoryid,
		    COUNT(DISTINCT orderNumber) AS total_order,
		    SUM(quantity) AS total_penjualan
	  FROM (
	  	  SELECT
	  		    productCode,
	  		    orderNumber,
	  		    quantity,
	  		    status,
	  		    SUBSTRING(productCode,1,3) AS categoryid
	  	  FROM
	  		    orders_2
	  	  WHERE
	  		    status="Shipped"
	  	   ) AS tabel_c
    GROUP BY
		    categoryid
    ) a
ORDER BY
	total_order DESC;

#[Seberapa banyak customers yang tetap aktif bertransaksi setelah transaksi pertamanya?](https://academy.dqlab.id/main/projectcode/246/421/2109)
#Menghitung total unik customers yang transaksi di quarter_1
SELECT 
    COUNT(DISTINCT customerID) as total_customers 
FROM 
    orders_1;
#output = 25

SELECT 
	  '1' AS quarter,
	  COUNT(DISTINCT customerID)*100/25 AS q2
FROM
	  orders_1
WHERE
	  customerID IN (
	  SELECT
	  	  DISTINCT(customerID)
	  FROM
	  	  orders_2
	  );
