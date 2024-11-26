DIRECTIONS = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2)
]

def knight_probability(n, k, r, c):
    dp = {}

    dp[(r, c, 0)] = 1  # Base case: probability = 1 at the starting position with 0 moves

    for step in range(1, k + 1):
        next_dp = {}
        for (row, col, prev_step), prob in dp.items():
            if prev_step != step - 1:
                continue  # Only process the previous step's states
            for dr, dc in DIRECTIONS:
                next_row, next_col = row + dr, col + dc
                if 0 <= next_row < n and 0 <= next_col < n:
                    next_dp[(next_row, next_col, step)] = (
                        next_dp.get((next_row, next_col, step), 0) + prob / 8
                    )
        dp = next_dp

    # Sum all probabilities from the final step
    result = sum(prob for (row, col, step), prob in dp.items() if step == k)
    return result

# Example usage
n = 6
k = 3
r = 2
c = 2
print(knight_probability(n, k, r, c))  # Bottom-Up
