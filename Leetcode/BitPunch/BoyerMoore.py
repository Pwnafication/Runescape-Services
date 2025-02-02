arrList = [1, 1, 1, 3, 3, 2, 4, 4, 4, 4, 4]

class Solution:
    def FindtheMode(self, arrList):
        # Step 1: Use Boyer-Moore to find a candidate for the mode
        candidate, count = None, 0
        for num in arrList:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        # Step 2: Verify the candidate and count its occurrences
        max_count = 0
        for num in arrList:
            if num == candidate:
                max_count += 1
        
        # Return the candidate and its count
        return f"Mode: {candidate}", f"{max_count}x"

Sol = Solution()
print(Sol.FindtheMode(arrList))  # Output: Mode: 4, 5x
