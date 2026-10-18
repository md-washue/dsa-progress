def anagram_subset(text,pattern):
    pattern_dic={}
    window_dic={}
    result = []
    left=0

    
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


    while left <= len(text) - len(pattern):
        if pattern_dic == window_dic:
            result.append(left)

        outgoing = text[left]
        window_dic[outgoing] -= 1

        if window_dic[outgoing] == 0:
            del window_dic[outgoing]

        left += 1
        right = left + len(pattern) - 1

        if right < len(text):
            incoming = text[right]
            window_dic[incoming] = window_dic.get(incoming, 0) + 1

    return result


    
text = "cbaebabacd"
pattern = "abc"
print(anagram_subset(text,pattern))

