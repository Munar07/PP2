a=int(input())
b=list(map(int,input().split()))
c=0
for x in b:
    if x>0:
        c=c+1
print(c)