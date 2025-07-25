heightArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]

def MaxContainerArea(heights):
    maxArea = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        height = min(heights[left], heights[right])  
        width = right - left
        area = height * width
        maxArea = max(maxArea, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return maxArea

print(MaxContainerArea(heightArray)) 


