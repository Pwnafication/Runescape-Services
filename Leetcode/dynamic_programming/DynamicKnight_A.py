DIRECTIONS = [
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2)
]

def knight_probability(n, k, row, column):
    if row < 0 or row >= n or column < 0 or column >= n:
        return 0

    if k == 0:
        return 1

    result = 0

    for dir in DIRECTIONS:
        result += knight_probability(n, k - 1, row + dir[0], column + dir[1]) / 8

    return result

# Example usage
n = 6
k = 3
row = 2
column = 2
print(knight_probability(n, k, row, column))
