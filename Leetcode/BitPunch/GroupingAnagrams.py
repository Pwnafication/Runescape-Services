daArray = ["eat", "tea", "ate", "bat","tan","nat"]

class Solution:
    def groupAnagrams(self, daArray):
        dct_AnagramMaps = {}
        for word in daArray:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in dct_AnagramMaps:
                dct_AnagramMaps[sorted_word] = [word]
            else: 
                dct_AnagramMaps[sorted_word].append(word)
        return list(dct_AnagramMaps.values())
            
Ans = Solution()
print(Ans.groupAnagrams(daArray))