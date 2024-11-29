SELECT 
    p.product_name,
    SUM(prod.quantity) as total_quantity
FROM 
    products p
JOIN 
    production prod ON p.product_id = prod.product_id
WHERE 
    prod.production_date = '2023-11-01'
GROUP BY 
    p.product_name
ORDER BY 
    total_quantity DESC;
