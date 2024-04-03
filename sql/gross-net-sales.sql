SELECT product_id,
       ROUND(gross_sale, 2) AS gross_sale,
       net_sale,
       ROUND(gross_sale - net_sale, 2) AS lost_to_discount
FROM (
    SELECT product_id, 
           SUM(unit_price * quantity_of_items_sold) AS gross_sale, 
           SUM((1 - discount) * unit_price * quantity_of_items_sold) AS net_sale
    FROM sales
    GROUP BY product_id
) AS subquery
ORDER BY gross_sale DESC;