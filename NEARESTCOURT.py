# cook your dish here
import math
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    z=abs(x-y)
    if z%2==0:
        n=z//2
        print(n)
    else:
        n=z//2
        print(n+1)
    