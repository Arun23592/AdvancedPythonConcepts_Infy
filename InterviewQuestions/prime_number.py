def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_prime(start, end):
    for num in range(start, end + 1):
        if prime_number(num):
            print(num)

calculate_prime(0,100)

