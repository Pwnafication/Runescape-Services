class Solution(object):
    def findLongestSubstring(self,string):
        subSet = set()
        leftIndex = 0
        result = 0
        for rightIndex in range(len(string)):
            while string[rightIndex] in subSet:
                subSet.remove(string[leftIndex])
                leftIndex += 1
            subSet.add(string[rightIndex])
            result = max(result, rightIndex - leftIndex + 1)
        return result
    
string = "aafdjsbvnsksiowhaklanamlaio"
theSolution = Solution()
print(theSolution.findLongestSubstring(string))
