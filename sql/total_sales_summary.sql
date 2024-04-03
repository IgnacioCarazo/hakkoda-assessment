CREATE TABLE total_sales_summary AS
SELECT 
    ROUND(SUM(unit_price * quantity_of_items_sold), 2) AS products_gross_sale,
    ROUND(SUM((1 - discount) * unit_price * quantity_of_items_sold), 2) AS products_net_sale,
    ROUND(SUM(unit_price * quantity_of_items_sold) - SUM((1 - discount) * unit_price * quantity_of_items_sold), 2) AS lost_to_discount
FROM 
    sales