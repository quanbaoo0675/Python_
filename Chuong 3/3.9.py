def decimal_to_hexadecimal(n):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16
    return hexadecimal

n = int(input())
print(f"Số thập lục phân của {n} là: {decimal_to_hexadecimal(n)}")