def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

n = int(input())
print(f"Số nhị phân của {n} là: {decimal_to_binary(n)}")