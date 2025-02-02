daArray = [1, 1, 2, 2, 3, 4, 4]

class Solution:
    def findSingles(self, daArray):
        dct_Numbers = {}
        last = None
        for each in daArray:
            if each in dct_Numbers:
                dct_Numbers[each] += 1
            else:
                dct_Numbers[each] = 1
            
            # Check if the previous number appeared only once
            if last is not None and dct_Numbers[last] == 1 and each != last:
                return last
            
            last = each
        
        # Final check in case the last number is the single one
        if last is not None and dct_Numbers[last] == 1:
            return last
        
        return None  # No single element found

Solution = Solution()
print(Solution.findSingles(daArray))  # Output: 3
