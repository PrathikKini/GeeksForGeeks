def filter_high_rated_expensive(df):
    # Code Here 
    return df[
        (df['product_id']>=4.5) &
        (df['quantity_in_stock'] > 0) &
        (df['price'] >= 300)
        ][['product_id','product_name','rating','quantity_in_stock','price']]