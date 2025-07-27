class Solution(object):
    def validAnagram(self, string1, string2):
        if len(string1) != len(string2):
            return False
        map1,map2 = {}, {}
        for index in range(len(string1)):
            map1[string1[index]] = map1.get(string1[index],0) + 1
            map2[string2[index]] = map2.get(string2[index],0) + 1
        for each in map1:
            if map1[each] != map2[each]:
                return False
        return True 
    
string1 = "asdf"
string2 = "adsf"
theSolution = Solution()
print(theSolution.validAnagram(string1,string2))