def ptb1(a, b):
    if a != 0:
        x = -b / a
        return x
    elif a == 0 and b != 0:
        return "VN"
    else:
        return "VSN"

a, b = map(int, input().split())
kq = ptb1(a, b)
print(kq)
