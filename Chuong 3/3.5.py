def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input("Nhập hai số nguyên dương a và b: ").split())
print(f"Bội chung nhỏ nhất của {a} và {b} là: {lcm(a, b)}")