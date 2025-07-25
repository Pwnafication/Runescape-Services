rainArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]

def GetWater(theArray):
    WaterCollected = 0  # Initialize total water collected
    for index, each in enumerate(theArray):  # Iterate through each position in the array
        
        varLeft = max(theArray[:index]) if index > 0 else 0 # Calculate the left boundary by finding the max height to the left of the current position
        varRight = max(theArray[index + 1:]) if index + 1 < len(theArray) else 0  # Calculate the right boundary by finding the max height to the right of the current position
        trappedWater = max(0, min(varLeft, varRight) - each) # The amount of water trapped at this position is the min of left and right boundaries minus the height at the current position
        WaterCollected += trappedWater # Add trapped water for this position to the total

    return WaterCollected

# Example usage
print(GetWater(rainArray))  # Expected output: Total water collected
