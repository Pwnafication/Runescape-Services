heightsArray = [4,8,1,2,3,9]

def MaxWater(theArray):
    p1 = 0
    p2 = len(theArray)-1
    MaxArea = 0 
    while p1 < p2:
        height = min(theArray[p1], theArray[p2])
        width = p2 - p1
        area = height * width
        MaxArea = max(area,MaxArea)
        if theArray[p1] <= theArray[p2]:
            p1 +=1 
        else:
            p2 -=1
    return MaxArea

print(MaxWater(heightsArray))