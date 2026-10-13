def max_package_pairs(weights, limit):
    left=0
    right= len(weights)-1
    match_list=[]
    while(left<=right):
        total=weights[left]+ weights[right]

        if(total == limit):
           answer=weights[left],weights[right]
           match_list.append(answer)
           left +=1
        #    break
        else:
            right -=1

    return(len(match_list))

    
   

weights = [1, 2, 3, 4, 5, 6]
limit = 7
# print(weights)

print(max_package_pairs(weights,limit))
