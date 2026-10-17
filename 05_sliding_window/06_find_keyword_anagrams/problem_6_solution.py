def anagram_subset(text,pattern):
    pattern_dic={}
    window_dic={}
    result = []

    
    for i in range (len(pattern)):
        if pattern[i] not in pattern_dic:
            pattern_dic[pattern[i]]= 1
        else:
            pattern_dic[pattern[i]] += 1

    for i in range(len(pattern)):
        if text[i] not in window_dic:
            window_dic[text[i]]=1
        else:
            window_dic[text[i]] +=1

    print(window_dic)
    if pattern_dic == window_dic:
        result.append(0)


# /////////not compeleted yet/////////////
    
text = "cbaebabacd"
pattern = "abc"
print(anagram_subset(text,pattern))

