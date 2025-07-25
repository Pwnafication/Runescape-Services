class Solution(object):
    def isValidParenthesis(self, theString):
        dct_Parenthesis = {
            "(" : ")",
            "[" : "]",
            "{" : "}",
        }

        StackBox = []

        if len(theString) == 0:
            return True
        if len(theString) == 1: 
            return False 
        
        for each in theString:
            if each in dct_Parenthesis:
                StackBox.append(each)
            else:
                if not StackBox:
                    return False
                Left = StackBox.pop()
                Right = dct_Parenthesis[Left]
                if Right != each:
                    return False
        if len(StackBox) == 0:
            return True
        else:
            return False


theString = "(){[]"
solution = Solution()
print(solution.isValidParenthesis(theString))

# 1. make dictionary 
# 1.5 make stack
# 2. do null checks
# 3. for each loop 
# 4. check if already empty 
# 5. if not empty, check if left matches right, by popping from stack 
# 6. if does not match, return false 
