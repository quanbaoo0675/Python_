# 4.2.8.	Viết chương trình nhập vào một xâu ký tự từ bàn phím. Chuẩn hóa xâu đó sao cho giữa hai từ chỉ có một dấu cách, đầu, cuối của xâu không có dấu cách, ký tự đầu của mỗi từ viết hoa, các ký tự còn lại viết thường.
# Ví dụ: đầu vào là “  nguyen     VAN    huNg    ”=>kết quả là “Nguyen Van Hung”

def chuanhoa():
    s = input()
    w = s.strip().split()
    chuanhoakitu = [word.capitalize() for word in w]
    kq = ' '.join(chuanhoakitu)
    print(kq)
chuanhoa()
