# cook your dish here
import math
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=math.ceil(y/z)
    print(x*k)