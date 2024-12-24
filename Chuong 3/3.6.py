def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
fibs = [fibonacci(i) for i in range(1, n + 1)]
print(f"Các số Fibonacci từ 1 đến {n}: {fibs}")
print(f"Tổng của chúng là: {sum(fibs)}")