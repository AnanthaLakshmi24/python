import math
# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    p=x/6
    k=math.ceil(p)
    print(k*y)