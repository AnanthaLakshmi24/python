# cook your dish here
import math
t=int(input())
for i in range(t):
    a,b,s=map(int,input().split())
    k=abs(a-b)
    print(math.ceil(k/s))