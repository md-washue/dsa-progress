def longest_unique_substring(s):
    unuique={}
    unuique_set=[]
    for item in s:
        if item not in unuique:
            unuique[item] = 0
            unuique_set.append(item)
        else:
            unuique[item] +=1

    return(len(unuique_set))


s = "abcabcbb"
print(longest_unique_substring(s))

