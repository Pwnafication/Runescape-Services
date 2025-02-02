class Solution:
    def generate_subsets(self, numbers):
        all_subsets = []  # List to store all subsets
        n = len(numbers)
        def backtrack(start_index: int, current_subset: list):
            all_subsets.append(current_subset)

            for index in range(start_index,n):
                current_subset.append(numbers[index])
                

            

        backtrack(0, [])
        return all_subsets


# Example usage
numbers = [1, 2]
solution = Solution()
result = solution.generate_subsets(numbers)
print("All Subsets:")
for subset in result:
    print(subset)
