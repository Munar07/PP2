N = int(input())
a, b = 0, 1
total = 0
while a <= N:
    total += a
    a, b = b, a + b
print(total)
