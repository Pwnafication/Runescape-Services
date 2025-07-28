class Solution:
    def checkInclusion(self, strTarget: str, strMain: str) -> bool:
        if len(strTarget) > len(strMain):
            return False

        targetCount = [0] * 26
        windowCount = [0] * 26
        for i in range(len(strTarget)):
            targetCount[ord(strTarget[i]) - ord('a')] += 1
            windowCount[ord(strMain[i]) - ord('a')] += 1

        matches = sum(1 for i in range(26) if targetCount[i] == windowCount[i])

        l = 0
        for r in range(len(strTarget), len(strMain)):
            if matches == 26:
                return True

            index = ord(strMain[r]) - ord('a')
            windowCount[index] += 1
            if targetCount[index] == windowCount[index]:
                matches += 1
            elif targetCount[index] + 1 == windowCount[index]:
                matches -= 1

            index = ord(strMain[l]) - ord('a')
            windowCount[index] -= 1
            if targetCount[index] == windowCount[index]:
                matches += 1
            elif targetCount[index] - 1 == windowCount[index]:
                matches -= 1
            l += 1

        return matches == 26
