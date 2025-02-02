daArray = [1, 2, 4, 5]
dct_Nums = {}

def FindMissingNumber(daArray):
    for each in daArray:
        dct_Nums[each] = each
    for each in daArray: 
        if each+1 not in dct_Nums:
            return each+1
    return "No missing numbers."


print(FindMissingNumber(daArray))  # Output: 3

#/////////////////////////////

daArray = [1, 2, 4, 5]

def FindMissingNumber(daArray):
    if not daArray:
        return "No numbers in the array."
    
    # Create a dictionary from the array
    dct_Nums = {each: 1 for each in daArray}

    # Check for the missing number
    for num in range(min(daArray), max(daArray)):
        if num not in dct_Nums:
            return num

    return "No missing numbers."

print(FindMissingNumber(daArray))  # Output: 3
