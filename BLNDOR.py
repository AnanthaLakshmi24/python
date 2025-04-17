# cook your dish here
import math
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    k=l.count(2)
    if k%8 == 0 :
        print("YES")
        
    else:
        print("NO")
            