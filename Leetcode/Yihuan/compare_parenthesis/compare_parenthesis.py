class Solution(object):
    def isValidParenthesis(self, theString):
        dct_Parenthesis = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        # Edge cases for empty or single character strings
        if len(theString) == 0:
            return True
        if len(theString) == 1:
            return False

        StackBox = []

        for each in theString:
            # Check if character is an opening bracket
            if each in dct_Parenthesis:
                StackBox.append(each)
            else:
                # Check if there's a corresponding opening bracket
                if not StackBox:
                    return False
                LeftBracket = StackBox.pop()
                RightBracket = dct_Parenthesis[LeftBracket]
                if RightBracket != each:
                    return False

        # If StackBox is empty, all brackets were matched
        return len(StackBox) == 0

# Testing the function
theString = "(){[]"
solution = Solution()
print(solution.isValidParenthesis(theString))  # Should return False for an unmatched opening bracket
