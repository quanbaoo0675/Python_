import math

def ptb2(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"x1 = {x1}, x2 = {x2}"
    
    elif delta == 0:
        x = -b / (2*a)
        return f"x1 = x2 = {x}"
    
    else:
        return "VN"
a, b, c = map(int, input().split())
kq = ptb2(a, b, c)
print(kq)
