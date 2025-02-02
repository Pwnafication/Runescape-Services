input_string = "aaabbca"
target = "aab"

class Solution:
    def smallestSubstring(self, input_string, target):
        string_length = len(input_string)
        target_length = len(target)
        
        if string_length < target_length:
            return "Does not compute..."

        hash_pattern = {}
        hash_string = {}

        # Create frequency map for the target
        for char in target:
            if char not in hash_pattern:
                hash_pattern[char] = 0
            hash_pattern[char] += 1

        left_p = 0
        count = 0
        min_len = float('inf')
        start_index = -1

        # Iterate over input_string to find the smallest substring
        for right_p, char in enumerate(input_string):
            if char not in hash_string:
                hash_string[char] = 0
            hash_string[char] += 1

            # If the character is in target and we haven't exceeded its count
            if char in hash_pattern and hash_string[char] <= hash_pattern[char]:
                count += 1

            # When we have a valid window
            if count == target_length:
                # Shrink the window from the left to minimize length
                while (input_string[left_p] not in hash_pattern or 
                       hash_string[input_string[left_p]] > hash_pattern[input_string[left_p]]):
                    if input_string[left_p] in hash_pattern:
                        hash_string[input_string[left_p]] -= 1
                    left_p += 1

                # Update minimum window length
                window_length = right_p - left_p + 1
                if min_len > window_length:
                    min_len = window_length
                    start_index = left_p

        if start_index == -1:
            return "No valid substring found"

        return input_string[start_index:start_index + min_len]

# Example usage
solution = Solution()
print(solution.smallestSubstring(input_string, target))  # Output: "aab"
