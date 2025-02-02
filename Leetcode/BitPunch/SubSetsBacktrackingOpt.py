class Solution:
    @staticmethod
    def generate_all_subsets(input_numbers):
        def recursive_generate_subsets(start_index, current_subset):
            all_subsets.append(current_subset[:])  # Add the current subset to the list of all subsets
            for current_index in range(start_index, len(input_numbers)):
                current_subset.append(input_numbers[current_index])  # Include the current number
                recursive_generate_subsets(current_index + 1, current_subset)  # Recurse for the next numbers
                current_subset.pop()  # Backtrack to explore other subsets

        all_subsets = []  # Initialize the list to hold all subsets
        recursive_generate_subsets(0, [])  # Start the recursive generation
        return all_subsets  # Return the complete list of subsets

# Example usage
input_numbers = [1, 2, 3, 4]
result = Solution.generate_all_subsets(input_numbers)
print("All Subsets:")
for subset in result:
    print(subset)
