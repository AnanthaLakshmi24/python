import math
# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    total=y*z 
    k=x/total
    print(math.ceil(k))