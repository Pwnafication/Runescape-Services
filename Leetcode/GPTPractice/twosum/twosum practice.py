class Solution(object):
    def findtwosum(self,nums,theTarget):
        num_dict = {}
        for i, each in enumerate(nums):
            complement = target - nums[i]
            if complement in num_dict:
                return [complement,nums[i]]
            else:
                num_dict[i] = complement
        return False

arr1 = [1, 3, 5, 7, 9]
target = 12
solution = Solution()
print(solution.findtwosum(arr1, target))  # Output: [1, 4] because 3 + 9 = 12
