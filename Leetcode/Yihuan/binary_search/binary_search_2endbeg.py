import math

numlist = [1, 3, 5, 5, 5, 5, 8, 9]
target = 5

class Solution(object):
    def BinarySearch(self, nums, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the midpoint
            midValue = nums[mid]
            if midValue == target:
                return mid
            elif midValue < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def SearchRange(self, numList, target):
        if len(numList) == 0:
            return [-1, -1]

        # Find first occurrence of the target
        firstPosition = self.BinarySearch(numList, 0, len(numList) - 1, target)
        if firstPosition == -1:
            return [-1, -1]

        # Initialize start and end positions
        startPos = firstPosition
        endPos = firstPosition

        # Expand startPos to the left
        tempPos = startPos
        while tempPos != -1:
            startPos = tempPos
            tempPos = self.BinarySearch(numList, 0, startPos - 1, target)

        # Expand endPos to the right
        tempPos = endPos
        while tempPos != -1:
            endPos = tempPos
            tempPos = self.BinarySearch(numList, endPos + 1, len(numList) - 1, target)

        return [startPos, endPos]


# Create an instance of Solution and test the functions
theSolution = Solution()
print("Binary Search Result:", theSolution.BinarySearch(numlist, 0, len(numlist) - 1, target))
print("Search Range Result:", theSolution.SearchRange(numlist, target))
