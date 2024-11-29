SELECT 
    e.employee_name,
    SUM(p.quantity) as total_quantity_produced
FROM 
    employees e
JOIN 
    production p ON e.employee_id = p.employee_id
GROUP BY 
    e.employee_name
ORDER BY 
    total_quantity_produced DESC;
