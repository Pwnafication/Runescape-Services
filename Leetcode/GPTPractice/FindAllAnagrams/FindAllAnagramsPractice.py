class Solution(object):
    def FindAllAnagrams(self, mainString, targetString):
        if len(targetString) > len(mainString): return []
        mainHash, targetHash = {}, {} 
        for index in range(len(targetString)): #init comps 
            mainHash[mainString[index]] = 1 + mainHash.get(mainString[index],0)
            targetHash[targetString[index]] = 1 + targetHash.get(targetString[index],0)
        
        result = [0] if mainHash == targetHash else []

        leftIndex = 0
        for rightIndex in range(len(targetString), len(mainString)):
            mainHash[mainString[rightIndex]] = 1 + mainHash.get(mainString[rightIndex],0)
            mainHash[mainString[leftIndex]] -=1
            if mainHash[mainString[leftIndex]] < 1: del mainHash[mainString[leftIndex]]
            leftIndex +=1
            if mainHash == targetHash: result.append(leftIndex)
        return result


# Example usage
mainString = "cbaebabacd"
targetString = "abc"
theSolution = Solution()
print(theSolution.FindAllAnagrams(mainString, targetString))  # Output: [0, 6]
