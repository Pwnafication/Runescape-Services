arr1 = [1, 3, 5, 8, 9]
target = 12

def findtwosum(theArray, theTarget):
    seen = {}  # Initialize an empty dictionary to store numbers and their indices
    for number in theArray:
        complement = theTarget - number  # Calculate the number needed to reach the target
        if complement in seen:
            return (complement, number)  # Return the pair if the complement is already in seen
        seen[number] = True  # Add the current number to the hash map as seen
    return None


print(findtwosum(arr1, target))
