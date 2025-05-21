QUERY = """
SELECT 
    m.order_number,
    m.order_date,
    m.payment_date,
    m.type AS order_type,
    pf.name AS payment_method,
    sm.name AS shipping_method,
    u_responsible.name AS responsible_name,
    r_responsible.description AS responsible_role,
    u_buyer.name AS buyer_name,
    r_buyer.description AS buyer_role,
    ms.name AS status,
    p.name AS product_name,
    c.name AS category_name,
    md.quantity,
    md.subtotal
FROM movement m
JOIN movement_detail md ON m.id = md.movement_id
JOIN product p ON md.product_id = p.id
LEFT JOIN product_category c ON p.product_category_id = c.id
LEFT JOIN user u_responsible ON m.responsible_id = u_responsible.id
LEFT JOIN rol r_responsible ON u_responsible.rol_id = r_responsible.id
LEFT JOIN user u_buyer ON m.buyer_id = u_buyer.id
LEFT JOIN rol r_buyer ON u_buyer.rol_id = r_buyer.id
LEFT JOIN payment_form pf ON m.payment_form_id = pf.id
LEFT JOIN shipping_method sm ON m.shipping_method_id = sm.id
LEFT JOIN movement_status ms ON m.movement_status_id = ms.id
"""
