a, b = map(int, input().split())

def squares(start, end):
    for i in range(start, end + 1):
        yield i * i

for value in squares(a, b):
    print(value)
