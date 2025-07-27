string = "a)bc(d)"

class Solution(object):
    def validate(self, string):
        arrayString = list(string)
        StackBox = [] 
        for index,each in enumerate(string):
            if each == "(":
                StackBox.append(index)
            else:
                if each == ")" and len(StackBox):
                    StackBox.pop()
                else:
                    if each == ")": 
                        arrayString[index] = ""
        while StackBox:
            for each in StackBox:
                arrayString[each] = ""
        return "".join(arrayString)

theSolution = Solution()
print(theSolution.validate(string))