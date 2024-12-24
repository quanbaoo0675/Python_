def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("): "))
primes = [i for i in range(1, n + 1) if is_prime(i)]
print(f"Các số nguyên tố trong khoảng (1, {n}): {primes}")
