# linear search


# def first_available_slot(slots):
#     answer=-1
#     available=True
#     for slot in slots:
#         if slot == available:
#             return slots.index(slot)


#     else:
#         return answer

#     # return(available_index)
# slots = [False, False,True, False]
# print(first_available_slot(slots))


# binary search

def first_available_slot(slots):
    left=0
    right=len(slots)-1
    result =-1
    while(left <=right):
        mid=(left+right)//2

        if (slots[mid]==True):
            result = mid
            right= mid-1

        else:
            left = mid+1
    return result     
    


# slots = [False, False, False, True, True, True]
# slots = [True, True, True]
# slots = [False, False, False, False]


print(first_available_slot(slots))
