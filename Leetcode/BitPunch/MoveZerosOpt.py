theNumbers = [1, 0, 0, 1, 1]

def MoveZeros(arr_Nums):
    p1 = 0
    p2 = 0
    n = len(arr_Nums)
    while p2 <= n - 1: 
        if arr_Nums[p2] != 0:
            arr_Nums[p1] = arr_Nums[p2]
            p1 +=1
        p2 +=1 

    for each in range(p1,n):
        arr_Nums[each] = 0
    
    return(arr_Nums)

print(MoveZeros(theNumbers))
