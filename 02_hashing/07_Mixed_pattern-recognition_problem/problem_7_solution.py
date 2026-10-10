def longest_stable_period(temperature, limit, maxFreq):
    n = len(temperature)
    longest = 0

    for left in range(n):
        for right in range(left, n):
            window = temperature[left:right + 1]

            if max(window) - min(window) > limit:
                continue

            freq = {}
            for t in window:
                freq[t] = freq.get(t, 0) + 1

            excess = sum(max(0, count - maxFreq)
                         for count in freq.values())

            if excess <= 1:
                longest = max(longest, len(window))

    return longest


temperature = [4, 2, 2, 3, 5, 2, 2, 4, 3]
limit = 3
maxFreq = 2
