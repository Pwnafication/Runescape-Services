daArray = [1, 1, 2, 2, 3, 4]

class Solution:
    def findSingles(self, daArray):
        result = 0
        for num in daArray:  # Iterate through daArray, not nums
            result ^= num  # XOR all numbers together
        return result  # Return the result after XORing

Solution = Solution()
print(Solution.findSingles(daArray))  # Output: 3
