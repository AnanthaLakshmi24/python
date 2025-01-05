# cook your dish here
import math
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if n%2==0:
        s=n//2
        if s==k:
            print("YES")
        else:
            print("NO")
    else:
        s=n/2 
        m=math.floor(s)
        p=math.ceil(s)
        if k==m or k==p:
            print("YES")
        else:
            print("NO")
        
        