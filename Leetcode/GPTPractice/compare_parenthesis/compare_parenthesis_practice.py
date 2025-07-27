class Solution(object):
    def isValid(self, theString):
        
        if len(theString) == 0:
            return True
        if len(theString) == 1:
            return False

        dct_Parenthesis = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        StackBox = []

        for each in theString:
            if each in dct_Parenthesis:
                StackBox.append(each)
            else:
                if not StackBox:
                    return False 
                left = StackBox.pop()
                right = dct_Parenthesis[left]
                if right != each: 
                    return False
        return len(StackBox) == 0 
                



theString = "(){[]"
theSolution = Solution()
print(theSolution.isValid(theString))