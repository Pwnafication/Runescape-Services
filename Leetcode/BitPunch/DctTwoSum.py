arr_sum = [2, 7, 11, 15]
target = 9

class Solution:
    def twoSum(self, arr, target):
        seen_numbers = {}
        for index, num in enumerate(arr):  # Track the index
            complement = target - num
            if complement in seen_numbers:
                return [seen_numbers[complement], index]  # Return indexes
            seen_numbers[num] = index  # Store the index in the map
        return "No pair found"

sol = Solution()
print(sol.find_two_sum(arr_sum, target))  # Output: [0, 1] (indexes of 2 and 7)
