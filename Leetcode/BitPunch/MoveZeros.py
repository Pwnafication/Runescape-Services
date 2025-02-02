arr_Numbers = [1, 0, 0, 1, 1]
n = len(arr_Numbers)
nonZeroCounter = 0
newArray = []

for each in arr_Numbers:
    if each != 0:
        newArray.append(each)
        nonZeroCounter +=1

for each in range(n - nonZeroCounter):
    newArray.append(0)
    
print(newArray)
