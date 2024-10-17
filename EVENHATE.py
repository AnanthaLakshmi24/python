import math
# cook your dish here
t=int(input())
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    odd=0
    even=0
    for i in range(n):
        if l[i] % 2==0:
            even=even+1
        else:
            odd=odd+1
    if odd==0:
        print(0)
    else:
        m=even+(odd-1)//2
        print(m+1)