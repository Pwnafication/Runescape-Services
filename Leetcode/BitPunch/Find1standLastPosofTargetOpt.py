arr_Numbers = [10, 11, 11, 11, 17, 18]
target = 11

def findTargetFirstAndLastPosition(daArray, target):
    p1 = 0
    p2 = len(daArray) - 1
    firstPosition = -1
    lastPosition = -1

    # Binary search for the first position
    while p1 <= p2:
        midIndex = (p1 + p2) // 2
        midValue = daArray[midIndex]
        if midValue == target:
            firstPosition = midIndex
            p2 = midIndex - 1  # Move left to find the first occurrence
        elif midValue < target:
            p1 = midIndex + 1
        else:
            p2 = midIndex - 1

    # Reset pointers for finding the last position
    p1 = 0
    p2 = len(daArray) - 1

    # Binary search for the last position
    while p1 <= p2:
        midIndex = (p1 + p2) // 2
        midValue = daArray[midIndex]
        if midValue == target:
            lastPosition = midIndex
            p1 = midIndex + 1  # Move right to find the last occurrence
        elif midValue < target:
            p1 = midIndex + 1
        else:
            p2 = midIndex - 1

    return (firstPosition, lastPosition)

# Example usage
print(findTargetFirstAndLastPosition(arr_Numbers, target))
