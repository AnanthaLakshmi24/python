# cook your dish here
t=int(input())
for i in range(t):
    n,k,p=map(int,input().split())
    l=list(map(int,input().split()))
    s=max(l)
    r=sum(l)
    u=r-s
    if (k+s)>(p+u):
        print("Ved")
    elif (k+s)==(p+u):
        print("Equal")
    else:
        print("Varun")