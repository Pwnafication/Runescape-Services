DIRECTIONS = [
    (-2, -1), (-2, 1), (-1, 2), (1, 2),
    (2, 1), (2, -1), (1, -2), (-1, -2)
]

def knight_probability(n, k, r, c):
    dp = {}
    dp[(r, c, 0)] = 1  # Base case: Probability = 1 at the starting position with 0 moves

    for step in range(1, k + 1):
        for row in range(n):
            for col in range(n):
                dp[(row, col, step)] = 0
                for dr, dc in DIRECTIONS:
                    prev_row, prev_col = row - dr, col - dc
                    if 0 <= prev_row < n and 0 <= prev_col < n:
                        dp[(row, col, step)] += dp.get((prev_row, prev_col, step - 1), 0) / 8

    # Sum all probabilities for positions after `k` moves
    result = 0
    for row in range(n):
        for col in range(n):
            result += dp.get((row, col, k), 0)

    return result

# Example usage
n = 6
k = 3
r = 2
c = 2
print(knight_probability(n, k, r, c))  # Bottom-Up Unoptimized
