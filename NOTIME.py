# cook your dish here
n,k,x=map(int,input().split())
l=list(map(int,input().split()))
ans="NO"
for i in l:
    if i+x>=k:
        ans="YES"
        break 
print(ans)