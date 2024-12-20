# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    degree=0
    for j in range(n-1,-1,-1):
        if l[j]!=0:
            degree=j
            break
    print(degree)