theString = "abcbdaac"

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        stringLength = len(s)
        p1, p2 = 0, 0
        ephemeralBox = set()
        char_index_map = {}
        MaxLength = 0
        
        while p2 < stringLength:
            print("Evaluating " + str(s[p2]))
            if s[p2] in ephemeralBox:

                p1 = char_index_map[s[p2]] + 1
                ephemeralBox = set(s[p1:p2])
            
            ephemeralBox.add(s[p2])
            char_index_map[s[p2]] = p2
            MaxLength = max(MaxLength,len(ephemeralBox))
            p2 += 1

        
        return MaxLength

solution = Solution()
print(solution.lengthOfLongestSubstring(theString))