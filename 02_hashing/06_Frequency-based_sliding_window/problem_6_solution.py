def character_replacement(s, k):

    count_values={}
    for item in s:
        if item not in count_values:
            count_values [item] = 1
        else:
            count_values[item] +=1


    # print(f"There are {max(count_values.values())}  ")

    most_common=max(count_values, key=count_values.get)
    # print(most_common)
    i=0

    new_list=[]

    for item in s:
        if item == most_common:
            new_list.append(item)
        else:
            if(i<k):
                item= most_common
                new_list.append(item)
                i+=1
            else:break

   

    return (len(new_list))


    
s = "AABABA"
k = 1
print(character_replacement(s,k))