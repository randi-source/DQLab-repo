#[Pengenalan Table - Customer](https://academy.dqlab.id/main/livecode/291/554/2776)
SELECT 
    * 
FROM 
    customer;

#[Pengenalan Table - Product](https://academy.dqlab.id/main/livecode/291/554/2777)
SELECT 
    * 
FROM 
    product;

#[Pengenalan Table - Subscription](https://academy.dqlab.id/main/livecode/291/554/2778)
SELECT 
    * 
FROM 
    subscription;

#[Pengenalan Table - Invoice](https://academy.dqlab.id/main/livecode/291/554/2779)
SELECT 
    * 
FROM 
    Invoice;

#[Pengenalan Table - Payment](https://academy.dqlab.id/main/livecode/291/554/2780)
SELECT 
    * 
FROM 
    payment;

#[Contoh penggunaan HAVING](https://academy.dqlab.id/main/livecode/291/555/2782)
SELECT 
    customer_id 
FROM 
    Subscription 
GROUP BY 
    customer_id 
HAVING 
    COUNT(customer_id) >1;

#[Menampilkan Konsumen yang berubah berlangganan](https://academy.dqlab.id/main/livecode/291/555/2783)
SELECT 
	  customer_id,
    product_id,
    subscription_date
FROM 
    Subscription 
WHERE 
    customer_id IN 
	  (SELECT 
         customer_id 
     FROM 
         Subscription 
     GROUP BY 
         customer_id 
     HAVING 
         COUNT(customer_id) > 1
  	) 
ORDER BY 
    customer_id ASC;

#[Menampilkan detail konsumen](https://academy.dqlab.id/main/livecode/291/555/2784)
SELECT b.name,
    b.address,
    b.phone, 
    a.product_id, 
    a.subscription_date 
FROM 
    subscription a 
JOIN 
    customer b 
ON 
    a.customer_id=b.id
WHERE b.id IN 
(
	  SELECT 
        customer_id 
    FROM 
        Subscription 
    GROUP BY 
        customer_id 
    HAVING 
        COUNT(customer_id) > 1
) 
ORDER BY 
    b.id ASC;

#[Penggunaan Fungsi MAX pada Having](https://academy.dqlab.id/main/livecode/291/556/2786)
SELECT 
    product_id, 
    MAX(total_price) AS total 
FROM 
    invoice 
GROUP BY 
    product_id;
SELECT 
    product_id, 
    MAX(total_price) AS total 
FROM 
    invoice 
GROUP BY 
    product_id 
HAVING 
    MAX(total_price) > 100000;
SELECT 
    product_id, 
    MAX(pinalty) AS total 
FROM 
    invoice
GROUP BY 
    product_id 
HAVING 
    MAX(pinalty) >30000;

#[Penggunaan Fungsi MIN pada Having](https://academy.dqlab.id/main/livecode/291/556/2787)
SELECT 
    product_id, 
    MIN(total_price) AS total 
FROM 
    invoice 
GROUP BY 
    product_id;
SELECT 
    product_id, 
    MIN(total_price) AS total 
FROM 
    invoice 
GROUP BY 
    product_id 
HAVING 
    MIN(total_price) <500000;
SELECT 
    product_id, 
    MIN(pinalty) AS total 
FROM 
    invoice 
GROUP BY 
    product_id 
HAVING 
    MIN(pinalty)<50000;

#[Penggunaan Fungsi AVG di Having](https://academy.dqlab.id/main/livecode/291/556/2788)
SELECT 
    product_id, 
    AVG(total_price) AS total 
FROM 
    invoice 
GROUP BY 
    product_id;
SELECT 
    product_id, 
    AVG(total_price) AS total 
FROM 
    invoice 
GROUP BY 
    product_id 
HAVING AVG(total_price) > 100000;
SELECT 
    product_id, 
    AVG(pinalty) AS total 
FROM 
    invoice 
GROUP BY 
    product_id 
HAVING 
    AVG(pinalty) > 30000;

#[Mini Quiz](https://academy.dqlab.id/main/livecode/291/556/2789)
SELECT 
    product_id, 
    AVG(pinalty),
    COUNT(customer_id) AS total 
FROM 
    invoice 
GROUP BY 
    product_id 
HAVING 
    COUNT(customer_id) >20; 				
