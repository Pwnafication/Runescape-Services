class Water(object):
    def LargestWaterContainer(self, nums):
        lIndex = 0
        rIndex = len(nums) - 1
        maxArea = 0

        while lIndex != rIndex:
            height = min(nums[lIndex], nums[rIndex])
            width = rIndex - lIndex
            area = height * width
            maxArea = max(maxArea, area)
            if nums[lIndex] < nums[rIndex]:
                lIndex += 1 
            else:
                rIndex -= 1
        return maxArea


heightNums = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]

problem = Water()
print(problem.LargestWaterContainer(heightNums))
