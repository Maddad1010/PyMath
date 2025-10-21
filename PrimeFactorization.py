# PrimeFactorization.py
# Program to find the prime factors of a number

# Function to find and print prime factors
def prime_factors(n):
    factors = []

    # Factor out 2s
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Factor out odd numbers
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2

    # If remaining n is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors


# Main program
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if num <= 1:
        print("Please enter a number greater than 1")
    else:
        result = prime_factors(num)
        print("Prime factors of", num, "are:", result)
