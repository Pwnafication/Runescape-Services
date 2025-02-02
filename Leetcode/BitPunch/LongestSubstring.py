subString = "abcdefgabcdefghzjbd"

def FindLongestSubstring(subString):
    dct_Letters = {}
    maxLength = 0
    for each in subString:
        if each not in dct_Letters:
            dct_Letters[each] = True
        else: 
            newLength = len(dct_Letters)
            if newLength > maxLength:
                maxLength = newLength
                dct_Letters = {}
                dct_Letters[each] = True
    return maxLength

print(FindLongestSubstring(subString))
        
