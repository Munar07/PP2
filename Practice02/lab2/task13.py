a=int(input())
if a<=1:
    print("No")
for i in range(2,int(a**0.5)+1):
    if(a%i==0):
        print("No")
        exit()
print("Yes")