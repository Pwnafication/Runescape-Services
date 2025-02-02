inString = "a)bc(d)"

class Solution(object):
    def minRemove(self, theString):
        arrString = list(theString)
        arrStack = []
        for index,each in enumerate(arrString):
            if each == "(":
                arrStack.append(index)
            else: 
                if each == ")" and len(arrStack):
                    arrStack.pop()
                else:
                    if each == ")":
                        arrString[index] = ""
        for each in arrStack: 
            currentIndex = arrStack.pop()
            arrString[currentIndex] = ""
        return "".join(arrString)

theSolution = Solution()
print(theSolution.minRemove(inString))