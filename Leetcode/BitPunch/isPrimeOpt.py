import math

number = 29

class Solution:
    def countPrimes(self, n: int) -> int:		
        if n < 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        
        for i in range(2, math.ceil(math.sqrt(n)) + 1):  # Correct loop range to include sqrt(n)
            if isPrime[i]:
                for multiples_of_i in range(i * i, n, i):
                    isPrime[multiples_of_i] = False
        
        return sum(isPrime)  # Sum of True values (primes)

# Instantiate the Solution class
solution = Solution()

# Call the method and print the result
print(solution.countPrimes(number))  # Output: 9 (prime numbers less than 29 are: 2, 3, 5, 7, 11, 13, 17, 19, 23)
