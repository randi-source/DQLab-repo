#[Overall Performance by Year](https://academy.dqlab.id/main/projectcode/182/358/1737)
SELECT 
    YEAR(order_date) AS years, 
    ROUND(SUM(sales),2) AS sales, 
    COUNT(order_id) AS number_of_order  
FROM 
    dqlab_sales_store
WHERE 
    order_status='Order Finished'
GROUP BY 
    1
ORDER BY 
    1;

#[Overall Performance by Product Sub Category](https://academy.dqlab.id/main/projectcode/182/358/1738)
SELECT
	  YEAR(order_date) as years,
	  product_sub_category,
	  SUM(sales) AS sales
FROM 
	  dqlab_sales_store
WHERE 
    YEAR(order_date)BETWEEN 2011 AND 2012
    AND order_status LIKE 'Order Finished'
GROUP BY 
	  years,
	  product_sub_category
ORDER BY 
	  years,
	  sales DESC;

#[Promotion Effectiveness and Efficiency by Years](https://academy.dqlab.id/main/projectcode/182/359/1758)
SELECT 
	  YEAR(order_date) AS years,
	  SUM(sales) AS sales,
	  SUM(discount_value) as promotion_value,
	  ROUND(SUM(discount_value)/SUM(sales)*100,2) AS burn_rate_percentage
FROM 
	  dqlab_sales_store
WHERE 
	  order_status='Order Finished'
GROUP BY 
	  years;

#[Promotion Effectiveness and Efficiency by Product Sub Category](https://academy.dqlab.id/main/projectcode/182/359/1759)
SELECT 
	  YEAR(order_date) AS years,
	  product_sub_category,
	  product_category,
	  SUM(sales) AS sales,
	  SUM(discount_value) AS promotion_value,
	  ROUND(SUM(discount_value)/SUM(sales)*100,2) AS burn_rate_percentage
FROM 
	  dqlab_sales_store
WHERE
	  order_status= 'Order Finished' AND
	  YEAR(order_date)= 2012
GROUP BY
	  years,
	  product_sub_category,
	  product_category
ORDER BY
	  sales DESC;

#[Customers Transactions per Year](https://academy.dqlab.id/main/projectcode/182/361/1760)
SELECT 
	  YEAR(order_date) AS years,
	  COUNT(DISTINCT customer) AS number_of_customer
FROM
	  dqlab_sales_store
WHERE
	  YEAR(order_date) BETWEEN 2009 AND 2012
	  AND order_status='Order Finished'
GROUP BY
	  years
ORDER BY
	  years;
