def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
print(f"Ước chung lớn nhất của {a} và {b} là: {gcd(a, b)}")