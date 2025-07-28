class Solution(object):
    def FindAllAnagrams(self, mainString, targetString):
        # If target is longer than main, no anagram possible
        if len(targetString) > len(mainString):
            return []

        # Initialize hashmaps to count character frequencies
        mainHash, targetHash = {}, {}

        # Build initial window and target hash frequency count
        for charIndex in range(len(targetString)):
            # Count chars in the first window of mainString
            mainChar = mainString[charIndex]
            mainHash[mainChar] = 1 + mainHash.get(mainChar, 0)

            # Count chars in the entire targetString
            targetChar = targetString[charIndex]
            targetHash[targetChar] = 1 + targetHash.get(targetChar, 0)

# mainHash   = {'a': 1, 'b': 1, 'c': 1}
# targetHash = {'a': 1, 'b': 1, 'c': 1}


        # Initialize result list
        # If the initial window matches the targetHash, add index 0
        result = [0] if mainHash == targetHash else []

        # Sliding window: start from len(targetString) to end of mainString
        leftIndex = 0
        for rightIndex in range(len(targetString), len(mainString)):
            # Character coming into the window
            newChar = mainString[rightIndex]
            mainHash[newChar] = 1 + mainHash.get(newChar, 0)

            # Character going out of the window (leftIndex)
            oldChar = mainString[leftIndex]
            mainHash[oldChar] -= 1

            # If count becomes 0, remove key to keep dicts comparable
            if mainHash[oldChar] == 0:
                del mainHash[oldChar]

            # Move left side of the window to the right
            leftIndex += 1

            # After sliding, compare updated mainHash to targetHash
            if mainHash == targetHash:
                result.append(leftIndex)  # Store current starting index

        return result


# Example usage
mainString = "cbaebabacd"
targetString = "abc"
theSolution = Solution()
print(theSolution.FindAllAnagrams(mainString, targetString))  # Output: [0, 6]
