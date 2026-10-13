def max_water(heights):
    left = 0
    right = len(heights) - 1
    max_area = 0

    while left < right:
        
        height = min(heights[left], heights[right])


        width = right - left



        area = height * width

        max_area = max(max_area, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area



heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# area = min(height_left, height_right) * (right - left)
print(max_water(heights))
