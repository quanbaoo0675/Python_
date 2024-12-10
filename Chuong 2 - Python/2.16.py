import math
a, b, c = map(int, input().split())

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Dien tich: {s:.2f}, Chu vi: {p * 2:.2f}")
else:
    print("Khong la tam giac")

    
