arr1 = [1, 3, 5, 8, 9]
target = 12

def findtwosum(nums, target):
    seen = {}  # Stores num: index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None  # If no solution is found



print(findtwosum(arr1, target))
