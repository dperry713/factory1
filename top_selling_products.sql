SELECT 
    p.product_name,
    SUM(o.quantity) as total_quantity_ordered
FROM 
    products p
JOIN 
    order_details o ON p.product_id = o.product_id
GROUP BY 
    p.product_name
ORDER BY 
    total_quantity_ordered DESC;
