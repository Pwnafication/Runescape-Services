integers = [1, 2, 3, 4]

class Solution:
    @staticmethod
    def set_of_sets(integers):
        bigList = [[]]  # Start with an empty set in the list
        for each in integers:
            for currentSet in bigList[:]:
                bigList.append(currentSet + [each])
        return bigList  # Return the list of all

# Example usage
result = Solution.set_of_sets(integers)
print("Subsets:")
for subset in result:
    print(subset)

