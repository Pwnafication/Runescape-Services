theArray = [5,9,2,1,4]

n = len(theArray)
maxVolume = 0
p1 = 0
p2 = n-1

while p1 < p2: 
    width = p2 - p1
    height = min(theArray[p1],theArray[p2])
    volume = width*height
    if maxVolume < volume:
        maxVolume = volume
    if theArray[p1] < theArray[p2]:
        p1 += 1
    else: p2 -= 1

print(maxVolume)

