lst = input().split()
n = int(input())

def limited_cycle(elements, times):
    for _ in range(times):
        for el in elements:
            yield el

first = True
for item in limited_cycle(lst, n):
    if not first:
        print(" ", end="")
    print(item, end="")
    first = False
