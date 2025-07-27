nums = [1, 2, 3, 4]

class Solution(object):
    def containsDuplicate(self, nums):
        mapBox = []
        left = 0
        while left < (len(nums)):
            if nums[left] not in mapBox:
                mapBox.append(nums[left]) 
                left +=1
            else:
                return True
        return False

theSolution = Solution()
print(theSolution.containsDuplicate(nums))