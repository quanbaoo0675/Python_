def tinhtong(x, n):
    if x == 1:
        return n + 1
    S = (1 - x**(n+1)) / (1 - x)
    return S
x, n = map(int, input().split())
S = tinhtong(x, n)
print(S)
