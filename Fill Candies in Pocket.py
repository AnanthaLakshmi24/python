# cook your dish here
import math 
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=y*z 
    print(math.ceil(x/k))