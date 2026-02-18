n = int(input())

def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

def primes_up_to(num):
    for i in range(2, num + 1):
        if is_prime(i):
            yield i

first = True
for p in primes_up_to(n):
    if not first:
        print(" ", end="")
    print(p, end="")
    first = False
