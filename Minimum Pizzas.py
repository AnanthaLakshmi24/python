import math
# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    k=x*y
    p=k/4
    print(math.ceil(p))