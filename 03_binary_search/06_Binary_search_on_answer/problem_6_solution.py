def min_capacity(weights, days):
    left = max(weights)
    right = sum(weights)
    result = right

    while left <= right:
        mid = (left + right) // 2

        current_weight = 0
        required_days = 1

        for weight in weights:

            if current_weight + weight > mid:
                required_days += 1

                current_weight = weight

            else:
                current_weight += weight

        if required_days <= days:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


weights = [3, 2, 2, 4, 1, 4]
# print(f"sum of list {sum(weights)}")
days = 3

print(min_capacity(weights, days))