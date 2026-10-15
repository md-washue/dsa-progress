# def longest_valid(products,k):
#     new_list=[]

#     i=0
#     for i in range(len(products)):
#         new_list.append(products[i])
#         for j in range(len(new_list)):

        
    
    
    
#     ...

# def longest_valid(products,k):
#     new_list=[]
#     i=0
#     for i in range(len(products)):
#         if(len(new_list)<k):
#             if products[i] not in new_list:
#                 new_list.append(products[i])
           
#         else:
#             if products[i] in new_list:
#                 new_list.append(products[i])

#     return new_list


# products = ["shoe", "bag", "shoe", "hat", "bag", "bag"]
# k = 2
# # longest_valid(products,k)
# print(longest_valid(products,k))




def longest_valid(products, k):
    freq = {}
    left = 0
    max_length = 0
    result = []

    for right in range(len(products)):
        freq[products[right]] = freq.get(products[right], 0) + 1

        while len(freq) > k:
            freq[products[left]] -= 1

            if freq[products[left]] == 0:
                del freq[products[left]]

            left += 1

        window_length = right - left + 1

        if window_length > max_length:
            max_length = window_length
            result = [products[left:right + 1]]

        elif window_length == max_length:
            result.append(products[left:right + 1])

    return result


products = ["shoe", "bag", "shoe", "hat", "bag", "bag"]
k = 2

print(longest_valid(products, k))



# !!!!!!

