CREATE TABLE total_net_by_store AS
SELECT 
    tc.store_id,
    ROUND(SUM(gns.net_sale), 2) AS total_net_sales
FROM 
    transactions_clean tc
JOIN 
    gross_net_sales gns ON tc.product_id = gns.product_id
GROUP BY 
    tc.store_id
ORDER BY tc.store_id ASC