n = int(input())

def squares(num):
    for i in range(1, num + 1):
        yield i * i

for value in squares(n):
    print(value)