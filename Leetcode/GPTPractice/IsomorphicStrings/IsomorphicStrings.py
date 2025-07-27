# string1 = "egg"
# string2 = "fgo"

# class Solution(object):
#     def isIsomorphic(self, string1, string2):
#         map1, map2 = {}, {}
#         for index in range(len(string1)):
#             char1, char2 = string1[index],string2[index]
#             if ((char1 in map1 and map1[char1] != char2) or (char2 in map2 and map2[char2] != char1)):
#                     return False
            
#             map1[char1] = char2
#             map2[char2] = char1
#         return True
    
# theSolution=Solution()
# print(theSolution.isIsomorphic(string1,string2))

string1 = "egg"
string2 = "foo"

class Solution(object):
    def isIsomorphic(self, string1, string2):
        map1, map2 = {}, {}
        for char1, char2 in zip(string1,string2):
            if ((char1 in map1 and map1[char1] != char2) or (char2 in map2 and map2[char2] != char1)):
                    return False
            
            map1[char1] = char2
            map2[char2] = char1
        return True
    
theSolution=Solution()
print(theSolution.isIsomorphic(string1,string2))