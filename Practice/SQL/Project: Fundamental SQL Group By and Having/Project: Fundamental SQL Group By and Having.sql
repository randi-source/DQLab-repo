#[Mendapatkan jumlah nilai pinalty](https://academy.dqlab.id/main/projectcode/292/558/2792)
SELECT 
	  customer_id, 
	  SUM(pinalty) 
FROM 
	  invoice
GROUP BY 
	  1 
HAVING 
	  SUM(pinalty) IS NOT NULL;

#[Mencari customer yang mengganti layanan](https://academy.dqlab.id/main/projectcode/292/558/2793)
SELECT 
	  t1.name AS name,
	  GROUP_CONCAT(t3.product_name)
FROM 
	  customer t1 
	JOIN 
		  subscription t2 ON t1.id = t2.customer_id 
	JOIN 
		  product t3 ON t2.product_id=t3.ID 
WHERE 
	t1.id IN (
	    SELECT
	        customer_id
	    FROM
	        subscription
	    GROUP BY
	        customer_id
	    HAVING
	        COUNT(1)>1
	    )
GROUP BY 
	1;
