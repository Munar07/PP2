a=int(input())
b=list(map(int,input().split()))
c=max(b)
for i,ch in enumerate(b, start=1):
    if ch==c:
        print(i)
        exit()