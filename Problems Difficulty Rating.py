# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    for i in range(n):
        if l[i]>=1000:
            s=s+1 
    print(s)