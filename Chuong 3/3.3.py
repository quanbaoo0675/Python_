def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

a, b = map(int, input().split())
perfect_numbers = [i for i in range(a, b + 1) if is_perfect(i)]
print(f"Các số hoàn hảo trong đoan ({a}, {b}): {perfect_numbers}")