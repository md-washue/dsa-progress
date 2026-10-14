def longest_health(activity, limit):
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(activity)):
        current_sum += activity[right]

        while current_sum > limit:
            current_sum -= activity[left]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

activity = [10, 20, 15, 5, 10, 10]

limit = 30

print(longest_health(activity,limit))