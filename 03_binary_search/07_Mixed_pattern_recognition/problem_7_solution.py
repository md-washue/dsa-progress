def next_warmer_period(temperatures):
    result = [0] * len(temperatures)

    stack = []

    for i in range(len(temperatures)):

        while stack and temperatures[i] > temperatures[stack[-1]]:
            previous = stack.pop() 

            result[previous] = i - previous

        stack.append(i) 

    return result


def first_temperature_at_least(temperatures, target):
    
    for i in range(len(temperatures)):

        if temperatures[i] >= target:
            return i

    return -1


temperatures = [30, 32, 31, 35, 34, 36, 33]
print(next_warmer_period(temperatures))
print(first_temperature_at_least(temperatures, 34))
