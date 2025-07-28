class Solution(object):
    def groupAnagrams(self, anagramsList): 

        dctGroups = {}

        for eachAnagram in anagramsList:
            anagramCode = [0] * 26

            for eachCharacter in eachAnagram:
                anagramCode[ord(eachCharacter) - ord("a")] += 1

            key = tuple(anagramCode)

            if key in dctGroups:
                dctGroups[key].append(eachAnagram)
            else:
                dctGroups[key] = [eachAnagram]

        return list(dctGroups.values())

anagrams = ["eat", "tea", "tan", "ate", "nat", "bat"]
theSolution = Solution()
print(theSolution.groupAnagrams(anagrams))