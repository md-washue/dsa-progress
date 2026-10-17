# # lists=[[1,2,45,5],[3,4,4,7,8],[3,4,2],[1,2,3]]
# # new_list=[]
# # mini_lenth=min(lists, key=len)
# # for list in lists:
    
# #     if len(list) == len(mini_lenth):
# #         new_list.append(list)
    


def min_subarray(target, prices):
    left = 0
    total = 0
    min_length = len(prices) + 1

    for right in range(len(prices)):
        
        total += prices[right]

        while total >= target:
            length = right - left + 1

            if length < min_length:

                min_length = length

            total -= prices[left]

            left += 1

    if min_length == len(prices) + 1:
        return 0

    return min_length


prices = [2, 3, 1, 2, 4, 3]
target = 7

print(min_subarray(target, prices)) 