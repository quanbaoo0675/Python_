def bpt1(a, b):
    if a > 0:
        x = -b / a
        return f"x > {x}"
    elif a < 0:
        x = -b / a
        return f"x < {x}"
    else:
        if b > 0:
            return "VSN"
        else:
            return "VN"
a, b = map(int, input().split())
kq = bpt1(a, b)
print(kq)
