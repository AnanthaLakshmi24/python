# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    r=[]
    c=0
    for i in range(n):
        if l[i]>c:
            r.append(1)
            c=l[i]
        else:
            r.append(0)
    for j in r:
        print(j,end=" ")