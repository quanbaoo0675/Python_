import math

def giaithua(n):
    S = 0
    for i in range(1, n + 1):
        S += math.factorial(i)
    return S
n = int(input())
kq = giaithua(n)
print(kq)
