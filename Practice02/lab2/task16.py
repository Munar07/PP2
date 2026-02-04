a=int(input())
b=list(map(int,input().split()))
number=set()
for x in b:
    if x not in number:
        print("YES")
        number.add(x)
    else:
        print("NO")