stringPalindrome = "racecar"

class Solution(object):
    def ValidatePalindrome(self, inputString, LeftPointer, RightPointer):
        while LeftPointer < RightPointer:
            if inputString[LeftPointer] != inputString[RightPointer]:
                return False
            LeftPointer +=1
            RightPointer -=1
        return True
             
    
    def CheckIfAtLeastAlmostaPalindrome(self, strCheck):
        StringLength = len(strCheck)
        LeftPointer = 0
        RightPointer = StringLength-1
        while LeftPointer < RightPointer:
            if strCheck[LeftPointer] != strCheck[RightPointer]:
                return (self.ValidatePalindrome(strCheck, LeftPointer + 1, RightPointer) or 
                        self.ValidatePalindrome(strCheck, LeftPointer, RightPointer - 1))
            LeftPointer +=1
            RightPointer -=1 
        return True

solution = Solution()
print(solution.CheckIfAtLeastAlmostaPalindrome(stringPalindrome))