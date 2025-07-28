class Solution:
    def checkInclusion(self, strTarget: str, strMain: str) -> bool:
        # If the target string is longer than the main string, no match possible
        if len(strTarget) > len(strMain):
            return False
        
        # Frequency counters for target and current window in main
        targetCount = [0] * 26
        windowCount = [0] * 26

        # Build initial counts from strTarget and first window of strMain
        for i in range(len(strTarget)):
            targetCount[ord(strTarget[i]) - ord('a')] += 1
            windowCount[ord(strMain[i]) - ord('a')] += 1

        # Count how many characters match in frequency
        matches = 0
        for i in range(26):
            if targetCount[i] == windowCount[i]:
                matches += 1

        # Slide the window across strMain
        l = 0  # left pointer
        for r in range(len(strTarget), len(strMain)):
            if matches == 26:
                return True

            # Character coming into the window
            index = ord(strMain[r]) - ord('a')
            windowCount[index] += 1
            if targetCount[index] == windowCount[index]:
                matches += 1
            elif targetCount[index] + 1 == windowCount[index]:
                matches -= 1

            # Character going out of the window
            index = ord(strMain[l]) - ord('a')
            windowCount[index] -= 1
            if targetCount[index] == windowCount[index]:
                matches += 1
            elif targetCount[index] - 1 == windowCount[index]:
                matches -= 1

            l += 1  # move window forward

        return matches == 26


# class Solution:
#     def checkInclusion(self, strTarget: str, strMain: str) -> bool:
#         if len(strTarget) > len(strMain):
#             return False

#         targetCount = [0] * 26
#         windowCount = [0] * 26
#         for i in range(len(strTarget)):
#             targetCount[ord(strTarget[i]) - ord('a')] += 1
#             windowCount[ord(strMain[i]) - ord('a')] += 1

#         matches = sum(1 for i in range(26) if targetCount[i] == windowCount[i])

#         l = 0
#         for r in range(len(strTarget), len(strMain)):
#             if matches == 26:
#                 return True

#             index = ord(strMain[r]) - ord('a')
#             windowCount[index] += 1
#             if targetCount[index] == windowCount[index]:
#                 matches += 1
#             elif targetCount[index] + 1 == windowCount[index]:
#                 matches -= 1

#             index = ord(strMain[l]) - ord('a')
#             windowCount[index] -= 1
#             if targetCount[index] == windowCount[index]:
#                 matches += 1
#             elif targetCount[index] - 1 == windowCount[index]:
#                 matches -= 1
#             l += 1

#         return matches == 26
