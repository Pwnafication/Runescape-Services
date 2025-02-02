import math 

numlist = [1,3,3,5,5,5,8,9]
target = 5
left = 0
right = len(numlist)-1

class Solution(object):
    def BinarySearch(self, nums, left, right, target):
        while left <= right:
            mid = math.floor((left + right)/2)
            midValue = nums[mid]
            if midValue == target:
                return mid
            else:
                if midValue < target:
                    left = mid+1
                else: 
                    right = mid-1

theSolution = Solution()
print(theSolution.BinarySearch(numlist, left, right, target))

