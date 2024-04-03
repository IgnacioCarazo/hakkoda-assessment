CREATE TABLE total_net_sales_by_category AS
SELECT 
    tc.category,
    ROUND(SUM(gns.net_sale), 2) AS total_net_sales
FROM 
    transactions_clean tc
JOIN 
    gross_net_sales gns ON tc.product_id = gns.product_id
GROUP BY 
    tc.category;