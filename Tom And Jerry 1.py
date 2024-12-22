# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d,k=map(int,input().split())
    dist=abs(b-d)+abs(a-c)
    if dist<=k and (k-dist)%2==0:
        print("Yes")
    else:
        print("No")