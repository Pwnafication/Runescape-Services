arr_FatNoobs = [3,2,3,2,1,1,2,1,3,2]

def findBoats(arr_FatNoobs):
    boats = 0
    n = len(arr_FatNoobs)
    constraint = 3
    arr_FatNoobs.sort()
    HeavyP = n-1
    LightP = 0

    while HeavyP >= LightP:
        if arr_FatNoobs[HeavyP] + arr_FatNoobs[LightP] > constraint:
            HeavyP -= 1
            boats +=1
        else: 
            HeavyP -= 1
            LightP += 1 
            boats += 1
         
    return boats 

print(findBoats(arr_FatNoobs))
            
