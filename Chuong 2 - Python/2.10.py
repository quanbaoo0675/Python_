import math

def bieuthuc(x, n):
    S = 1
    for _ in range(n):
        S = 1 + math.sqrt(x + S)
    return S

x, n = map(int, input().split())
kq = bieuthuc(x, n)
print(kq)
