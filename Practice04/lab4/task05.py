n = int(input())

def countdown(num):
    for i in range(num, -1, -1):
        yield i

for value in countdown(n):
    print(value)
