# cook your dish here
l=list(map(int,input().split()))
ans=0
for i in range(len(l)):
    if l[i]>=10:
        ans=ans+1
print(ans)