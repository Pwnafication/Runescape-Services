arrList = [1,1,1,3,3,2,4,4,4,4,4]

class Solution:
    def FindtheMode(self, arrList):
        dct_list = {}
        maxValue, mode = 0
        for each in arrList:
            if each not in dct_list:
                dct_list[each] = 0
            dct_list[each] += 1
            if dct_list[each] > maxValue:
                maxValue = dct_list[each]
                mode = each
        return f"Mode: {mode}",f"{maxValue}x"

Sol = Solution()
print(Sol.FindtheMode(arrList))