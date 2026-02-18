a=int(input())
x=2
while x<=a//2:
    if a%x==0:
        print("No")
        exit()
    x+=1
print("Yes")