n = int(input())

def fibonacci(count):
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b

first = True
for num in fibonacci(n):
    if not first:
        print(",", end="")
    print(num, end="")
    first = False
