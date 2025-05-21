def transform_data(df):
    df_filled = df.fillna("N/A")

    df_details = df_filled[[
        'order_number', 'order_date', 'product_name', 'category_name', 'quantity', 'subtotal'
    ]]

    df_summary = df_filled.groupby([
        'order_number', 'order_date', 'payment_date', 'order_type', 'payment_method',
        'shipping_method', 'responsible_name', 'responsible_role', 'buyer_name',
        'buyer_role', 'status'
    ], as_index=False).agg({
        'subtotal': 'sum'
    }).rename(columns={'subtotal': 'total'})

    return df_details, df_summary