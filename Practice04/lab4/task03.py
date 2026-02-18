n = int(input())

def divisible(num):
    for i in range(0, num + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

first = True
for x in divisible(n):
    if not first:
        print(" ", end="")
    print(x, end="")
    first = False
