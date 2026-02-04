a = list(map(int, input().split()))
arr = list(map(int, input().split()))
l = a[1] - 1 
r = a[2] - 1
arr[l:r+1] = arr[l:r+1][::-1]
print(*arr)
