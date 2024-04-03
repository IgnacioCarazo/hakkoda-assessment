CREATE TABLE sales_percentage AS
WITH ProductSales AS (
    SELECT 
        product_id,
        SUM(unit_price * quantity_of_items_sold) AS total_sales
    FROM 
        sales
    GROUP BY 
        product_id
),
TotalSales AS (
    SELECT 
        SUM(unit_price * quantity_of_items_sold) AS overall_total_sales
    FROM 
        sales
)
SELECT 
    ps.product_id,
    ps.total_sales,
    round((ps.total_sales / ts.overall_total_sales) * 100,2) AS percentage_of_total_sales
FROM 
    ProductSales ps
CROSS JOIN 
    TotalSales ts
ORDER BY percentage_of_total_sales DESC;