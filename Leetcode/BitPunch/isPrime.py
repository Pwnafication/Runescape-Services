
number = 29

def isPrime(number):
    if number <= 0:
        return False
    if number == 1:
        return True
    for each in range(2,number):
        if number % each == 0:
            return False
    return True
print(isPrime(number))
