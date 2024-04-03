CREATE TABLE sold_by_client_per_store AS
SELECT 
    tc.store_id,
    tc.client_id,
    tc.product_id,
    ROUND(SUM(gns.net_sale), 2) AS total_net_sales
FROM 
    transactions_clean tc
JOIN 
    gross_net_sales gns ON tc.product_id = gns.product_id
GROUP BY
    tc.store_id,
    tc.client_id,
    tc.product_id
ORDER BY 
    tc.client_id ASC;