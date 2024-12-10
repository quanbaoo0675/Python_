def hpt(a1, b1, c1, a2, b2, c2):
    delta = a1 * b2 - a2 * b1

    if delta != 0:
        x = (c1 * b2 - c2 * b1)
        y = (a1 * c2 - a2 * c1)
        return f"x = {x}, y = {y}"
    elif delta == 0:
        if a1 * c2 == a2 * c1:
            return "VSN"
        else:
            return "VN"

a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
kq = hpt(a1, b1, c1, a2, b2, c2)
print(kq)
