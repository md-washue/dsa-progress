# nested_loop_search

# def two_sum(scores, target):
#     for i in range (len(scores)):
#         for j in range(i+1, (len(scores))):
#             add=scores[i]+scores[j]
#             if (add==target):
#                 print(scores.index(scores[i]),scores.index(scores[j]))
#     ...
# scores = [1, 3, 4, 6, 8,9, 11]
# target = 10
# two_sum(scores,target)



# two_pointer_serch


def two_sum(scores, target):
    left=0
    right=len(scores)-1
    while (left<=right):
        add=scores[left]+scores[right]
        if(add == target):
            print(scores.index(scores[left]),scores.index(scores[right]))
            left +=1
            right -=1
            # break
        elif(add<target):
            left +=1
        else:
            right -=1
    ...



scores = [1, 3, 4, 6, 8, 11]
scores = [1, 3, 4, 6, 8, 9, 11]
target = 10
# print(len(scores)-1)

two_sum(scores,target)