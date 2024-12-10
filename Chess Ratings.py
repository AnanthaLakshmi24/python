import math
# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>=y:
        print(0)
    else:
        k=y-x 
        print(math.ceil(k/8))