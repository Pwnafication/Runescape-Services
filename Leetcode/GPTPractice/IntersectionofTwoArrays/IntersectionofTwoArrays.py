arr1 = [6,3,7]
arr2 = [1,3,4,5,6,6]

class Solution(object):
    def IntersectsAt(self, arr1,arr2):
        set1 = set(arr1)
        set2 = set()
        for each in arr2:
            if each not in set2 and each in set1:
                set2.add(each)
        return set2

theSolution = Solution()
print(theSolution.IntersectsAt(arr1,arr2))

        
