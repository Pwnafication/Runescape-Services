arr1 = [1,3,5,7,9]
target = 12

def findtwosum(theArray, theTarget):
    for eachP1 in range(len(theArray)):
        for eachP2 in range(eachP1+1, len(theArray)):
            if theArray[eachP1] + theArray[eachP2] == theTarget:
                return (theArray[eachP1], theArray[eachP2])
    return None

print(findtwosum(arr1,target))

