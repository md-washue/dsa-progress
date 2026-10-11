def search_product(product_ids, target):
    location=-1
    for product_id in product_ids:
        if (product_id==target):
            location=product_ids.index(product_id)

    return (location)
        


product_ids = [101, 108, 115, 123, 140, 155, 170]
print(search_product(product_ids, 130))
