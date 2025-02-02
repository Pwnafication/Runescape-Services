class Solution:
    @staticmethod
    def comboIterator(lis_integers, int_target, bigAnsList, curList, pointer, cur_sum):
        # If the sum matches the target, add the current combination to the results
        if cur_sum == int_target:
            bigAnsList.append(curList[:])  # Append a copy of the current list
            return
        # If the sum exceeds the target, return to stop further exploration
        elif cur_sum > int_target:
            return

        # Iterate through the numbers starting from the current pointer
        n = len(lis_integers)
        for i in range(pointer, n):
            curList.append(lis_integers[i])  # Choose the current number
            Solution.comboIterator(lis_integers, int_target, bigAnsList, curList, i, cur_sum + lis_integers[i])  # Explore further
            curList.pop()  # Backtrack to explore other possibilities

    @staticmethod
    def findCombos(lis_integers, int_target):
        bigAnsList = []  # To store all valid combinations
        Solution.comboIterator(lis_integers, int_target, bigAnsList, [], 0, 0)
        return bigAnsList


# Example usage
lis_integers = [1, 3, 5, 7]
int_target = 10
result = Solution.findCombos(lis_integers, int_target)
print("Combinations that sum to target:")
print(result)
