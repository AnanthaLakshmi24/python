n=int(input())
l=list(map(int,input().split()))
res=[]
for i in range(n):
    if l[i]%2!=0:
        res.append(l[i])
print(res[-1])