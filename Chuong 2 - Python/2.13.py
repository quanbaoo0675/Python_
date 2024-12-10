import math
n = 1
S_sum = 0
while S_sum <= 1000:
    S_sum += n
    n += 1
print(n - 1)
n = 1000
S = 1
for i in range(1, n + 1):
    S += 1 / math.factorial(2 * i + 1)
print(S)
