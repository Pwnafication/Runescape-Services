daArray = [1, 2, 4, 5]

def FindMissingNumber(daArray):
    daArray.sort()  # Sort the array in-place
    n = len(daArray)

    for i in range(n - 1):  # Loop through indices of the sorted array
        if daArray[i] + 1 != daArray[i + 1]:
            return daArray[i] + 1  # Return the missing number if found

    return None  # Return None if no missing number is found

print(FindMissingNumber(daArray))  # Output: 3
