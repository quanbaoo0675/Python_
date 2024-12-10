x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())

area = abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2)

if area == 0:
    print("Ba diem khong tao thanh tam giac)
else:
    print("Ba diem tao thanh tam giac)
