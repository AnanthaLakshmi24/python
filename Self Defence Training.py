# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for j in range(n):
        if l[j]>=10 and l[j]<=60:
            c=c+1 
    print(c)