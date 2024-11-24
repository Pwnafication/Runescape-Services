# 2 strings
first_string = "hellooo##"
second_string = "hee#lll#o"

class Solution:
    def check_arrays_equal(arr1, arr2):
        ephemeralCounter = 0
        p1 = len(arr1) - 1
        p2 = len(arr2) - 1

        while p1 >= 0 or p2 >= 0:
            # Handle backspaces for arr1
            if p1 >= 0 and arr1[p1] == "#":
                ephemeralCounter += 2
            while ephemeralCounter > 0 and p1 >= 0:
                p1 -= 1
                ephemeralCounter -= 1
                if p1 >= 0 and arr1[p1] == "#":
                    ephemeralCounter += 2

            # Handle backspaces for arr2
            if p2 >= 0 and arr2[p2] == "#":
                ephemeralCounter += 2
            while ephemeralCounter > 0 and p2 >= 0:
                p2 -= 1
                ephemeralCounter -= 1
                if p2 >= 0 and arr2[p2] == "#":
                    ephemeralCounter += 2

            # After processing backspaces, compare characters
            if p1 >= 0 and p2 >= 0:
                if arr1[p1] != arr2[p2]:
                    return False
            elif p1 >= 0 or p2 >= 0:
                # If one string has characters left after backspace processing, they are not equal
                return False

            # Move to the next character
            p1 -= 1
            p2 -= 1

        return True

# Test the function
print(Solution.check_arrays_equal(first_string, second_string))  # Expected output: True
