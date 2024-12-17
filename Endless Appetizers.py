import math
# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    p=z//30
    k=x+p
    print(math.ceil(k/y))