def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

num = int(input())
print(f"Tổng các chữ số của {num} là: {sum_of_digits(num)}")