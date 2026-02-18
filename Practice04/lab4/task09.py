n = int(input())

def powers_of_two(num):
    i = 0
    while i <= num:
        yield 2 ** i
        i += 1

first = True
for val in powers_of_two(n):
    if not first:
        print(" ", end="")
    print(val, end="")
    first = False
