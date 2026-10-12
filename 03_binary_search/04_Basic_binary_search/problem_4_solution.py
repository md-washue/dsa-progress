# def search_product(product_ids, target):
#     location=-1
#     for product_id in product_ids:
#         if (product_id==target):
#             location=product_ids.index(product_id)

#     return (location)
        


# product_ids = [101, 108, 115, 123, 140, 155, 170]
# print(search_product(product_ids, 130))

# //////binary_search/////////



def search_product(product_ids, target):
    location=-1
    left=0
    right=len(product_ids)-1
    while(left<=right):
        mid=(left+right)//2
        if(product_ids[mid] ==target):
            location=mid
            return location
        elif(target <product_ids[mid]):
            right = mid-1
        else:
            left = mid+1
            
    return location
product_ids = [101, 108, 115, 123, 140, 155, 170]
print(search_product(product_ids,140))
