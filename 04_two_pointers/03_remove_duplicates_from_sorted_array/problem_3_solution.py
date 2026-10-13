def remove_duplicates(product_ids):
    left = 0
    right= len(product_ids)-1
    organized_list=[]
    while(left <=right):
        if product_ids[left] not in organized_list :
            organized_list.append(product_ids[left])
            # organized_list.append(product_ids[right])
        else:
            left +=1
            # right -=1

    return len(organized_list)

    ...
product_ids = [1, 1, 2, 2, 3, 4, 4]
print(remove_duplicates(product_ids))