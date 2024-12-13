import math
# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    k=y/100
    p=math.ceil(k)
    if x<=p:
        print(p-x)
    else:
        print(0)