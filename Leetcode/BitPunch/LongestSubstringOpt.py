subString = "abcdefgabcdefghzjbd"
def FindLongestSubstring(subString):
    dct_Letters = {}
    maxLength = 0
    n = len(subString)
    p1 = 0
    p2 = 0
    while p2 < n:
        character = subString[p2]
        if character in dct_Letters:
            p1 = dct_Letters[character] + 1
        dct_Letters[character] = p2
        maxLength = max(maxLength,(p2-p1)+1)
        p2 += 1 
    return maxLength

print(FindLongestSubstring(subString))


