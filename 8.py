# Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.

def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
                break
        else:
            return True


print(is_prime(9))
