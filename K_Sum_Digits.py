n = int(input())
x = int(input())
sum_digits = 0

while x > 0:
    digit = x % 10
    sum_digits += digit
    x = x // 10

print(sum_digits)
