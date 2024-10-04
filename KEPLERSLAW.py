# cook your dish here
import math
t=int(input())
for j in range(t):
    x,y,z,p=map(int,input().split())
    k=(math.pow(x,2))/(math.pow(z,3))
    l=(math.pow(y,2))/(math.pow(p,3))
    if k==l:
        print("Yes")
    else:
        print("No")
    