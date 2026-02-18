n = int(input())

def even_numbers(num):
    i = 0
    while i <= num:
        yield i
        i += 2

first = True
for x in even_numbers(n):
    if not first:
        print(",", end="")
    print(x, end="")
    first = False
