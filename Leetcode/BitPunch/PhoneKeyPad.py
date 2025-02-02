from typing import List

class Solution:
    def backtracking(self, ans: List[str], m: dict, digits: str, combination: str, index: int):
        # Base case: if we've reached the end of the digits
        if index == len(digits):
            ans.append(combination)
            return
        
        # Get the current digit and corresponding letters
        current_digit = digits[index]
        possible_letters = m[current_digit]

        # Explore all possible letters for the current digit
        for letter in possible_letters:
            self.backtracking(ans, m, digits, combination + letter, index + 1)

    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case: empty input
        if not digits:
            return []

        # Mapping of digits to letters
        m = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        ans = []
        self.backtracking(ans, m, digits, "", 0)
        return ans

# Example usage:
solution = Solution()
digits = "23"
print(solution.letterCombinations(digits))  # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
