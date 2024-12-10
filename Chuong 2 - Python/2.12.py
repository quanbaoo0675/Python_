import math

def giaithua(n):
    S = 0
    for i in range(0, n + 1):
        S += math.factorial(2 * i + 1)
    return S
n = int(input())
kq = giaithua(n)
print(kq)
