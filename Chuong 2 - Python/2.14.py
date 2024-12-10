import math

a = float(input())
S = 1
n = 1
term = 1 / math.factorial(2 * n + 1)
while term >= a:
    S += term
    n += 1
    term = 1 / math.factorial(2 * n + 1)

print(S)
