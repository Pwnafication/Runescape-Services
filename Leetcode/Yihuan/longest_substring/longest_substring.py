#bruteForce

#string
theString = "abcbdaac"

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        p1 = 0
        p2 = 0
        MaxString = 0
        for _ in s:
            ephemeralBox = []  # Reset ephemeralBox for each new starting point
            while p1 < len(s):
                print("Evaluating " + str(s[p1]))
                if s[p1] in ephemeralBox:
                    print("Character already in box, breaking out of loop.")
                    break  # Stop current while loop as soon as a duplicate is found
                else:
                    print("Adding to box.")
                    ephemeralBox.append(s[p1])
                MaxString = max(MaxString, len(ephemeralBox))
                p1 += 1
            print("Resetting...")
            p2 += 1
            p1 = p2  # Move the starting point for the next substring
        return MaxString

# Instantiate the Solution class
solution = Solution()
print(solution.lengthOfLongestSubstring(theString))