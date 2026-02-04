a=int(input())
b=list(map(int,input().split()))
freq={}
for x in b:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
max_freq=max(freq.values())
minimum=min(x for x in freq if freq[x]==max_freq)
print(minimum)