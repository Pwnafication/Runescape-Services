inString = "a)bc(d)"

class Solution(object):
    def minRemove(self, theString):
        arrString = list(theString)
        StackBox = []
        for index,each in enumerate(arrString):
            if each == "(":
                StackBox.append(index)
            else: 
                if each == ")" and len(StackBox) > 0:
                    currentItem = StackBox.pop()
                else: 
                    if each == ")" and len(StackBox) < 1:
                        arrString[index] = ""
        for each in StackBox:
            StackBox.pop()
            arrString[each] = "" 
        return "".join(arrString)
                
theSolution = Solution()
print(theSolution.minRemove(inString))

