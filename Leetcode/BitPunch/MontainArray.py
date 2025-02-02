def is_mountain_array(theArray):
    n = len(theArray)
    if n < 3:
        return False
    i = 0
    while i + 1 < n and theArray[i] < theArray[i + 1]:
        i += 1
    if i == 0 or i == n - 1:
        return False
    while i + 1 < n and theArray[i] > theArray[i + 1]:
        i += 1
    return i == n - 1

theArray = [0, 3, 2, 1]
print(is_mountain_array(theArray))
