#choose,explore,return

str_checkMe = "aab"

class Solution:

    @staticmethod
    def isPalindrome(str_ItemtoCheckPalindrome):
        i = 0
        j = len(str_ItemtoCheckPalindrome) - 1
        while i <= j:
            if str_ItemtoCheckPalindrome[i] != str_ItemtoCheckPalindrome[j]:
                return False
            else:
                i += 1
                j -= 1
        
    @staticmethod
    def iterator(in_str_input,answerList,currentAnswer, index):
        


    @staticmethod
    def findPalindromes(in_str_input):
        answerList = []
        currentAnswer = []
        return iterator(in_str_input,answerList,currentAnswer,0)
        
print(Solution.findPalindromes(str_checkMe))