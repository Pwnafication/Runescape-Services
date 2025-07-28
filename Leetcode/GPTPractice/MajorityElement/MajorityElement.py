class Solution(object):
    def getMajorityElement(self, nums):
        dctCount = {} 
        result, maxCount = 0, 0

        for eachNumber in nums:
            dctCount[eachNumber] = 1 + dctCount.get(eachNumber, 0)

            if dctCount[eachNumber] > maxCount:
                result = eachNumber
                maxCount = dctCount[eachNumber]

        return result
