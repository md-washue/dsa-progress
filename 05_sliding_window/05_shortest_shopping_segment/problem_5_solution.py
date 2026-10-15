lists=[[1,2,45,5],[3,4,4,7,8],[3,4,2],[1,2,3]]
new_list=[]
mini_lenth=min(lists, key=len)
for list in lists:
    
    if len(list) == len(mini_lenth):
        new_list.append(list)
    


print(new_list)
# print(min(array))