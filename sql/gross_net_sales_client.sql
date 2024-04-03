CREATE TABLE gross_net_sales_client AS
SELECT client_id,
       ROUND(gross_sale, 2) AS gross_sale,
       Round(net_sale, 2),
       ROUND(gross_sale - net_sale, 2) AS lost_to_discount
FROM (
    SELECT client_id, 
           SUM(unit_price * quantity_of_items_sold) AS gross_sale, 
           SUM((1 - discount) * unit_price * quantity_of_items_sold) AS net_sale
    FROM sales
    GROUP BY client_id
) AS subquery
ORDER BY client_id ASC;