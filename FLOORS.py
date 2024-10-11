import math
# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    s=math.ceil(x/10)
    p=math.ceil(y/10)
    diff=abs(s-p)
    print(diff)