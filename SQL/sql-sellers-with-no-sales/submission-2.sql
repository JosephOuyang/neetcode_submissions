-- Write your query below
WITH orders_2020 AS (
    SELECT seller_id FROM orders
    WHERE EXTRACT(YEAR FROM sale_date) = 2020
)

SELECT seller_name FROM seller 
WHERE seller_id NOT IN (SELECT seller_id FROM orders_2020)
ORDER BY seller_name ASC;