g = 0  # global variable

def outer(commands):
    n = 0  # outer function local variable

    def inner():
        nonlocal n
        global g

        for scope, value in commands:
            if scope == "global":
                g += value
            elif scope == "nonlocal":
                n += value
            # 'local' does nothing for g or n

    inner()
    return n

# read input
N = int(input())
commands = []
for _ in range(N):
    scope, val = input().split()
    commands.append((scope, int(val)))

n_final = outer(commands)
print(f"{g} {n_final}")
