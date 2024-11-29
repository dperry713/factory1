SELECT 
    c.customer_name,
    SUM(o.order_total) as total_order_value
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_name
HAVING 
    SUM(o.order_total) >= 10000
ORDER BY 
    total_order_value DESC;
