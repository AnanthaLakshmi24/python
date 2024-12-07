# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for j in range(x):
        if l[j]>=y:
            c=c+1
    print(c)