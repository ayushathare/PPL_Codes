def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(n):
    prime_numbers = []
    for num in range(2, n + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

n = int(input("Enter the value of n: "))
print("Prime numbers between 0 and", n, "are:", find_primes(n))
