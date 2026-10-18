def max_segment(visits, k):
    window_dic = {}
    left = 0
    max_freq = 0
    result = 0

    for right in range(len(visits)):
        ch = visits[right]
        window_dic[ch] = window_dic.get(ch, 0) + 1

        max_freq = max(max_freq, window_dic[ch])

        while (right - left + 1) - max_freq > k:
            window_dic[visits[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


visits = "AABABBA"
k = 1
print(max_segment(visits, k))
