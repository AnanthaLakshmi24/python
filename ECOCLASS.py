# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    s=list(map(int,input().split()))
    d=list(map(int,input().split()))
    c=0
    for j in range(x):
        if s[j]==d[j]:
            c=c+1
    print(c)