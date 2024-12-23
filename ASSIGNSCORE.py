# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=sum(l)
    p=(n+1)*100/2
    r=p-c 
    if r<=0:
        print(0)
    elif r>100:
        print(-1)
    else:
        print(int(r))