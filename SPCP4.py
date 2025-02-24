# cook your dish here
import math
t=int(input())
for _ in range(t):
    n,x,k=map(int,input().split())
    rem_boy=x%k
    rem_girls=(n-x)%k
    rem_read=(rem_boy+rem_girls)-2*min(rem_boy,rem_girls)
    print(rem_read)