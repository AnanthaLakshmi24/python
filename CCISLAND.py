# cook your dish here
# cook your dish here
t=int(input())
for i in range(t):
    x,y,p,q,d=map(int,input().split())
    r=x//p
    s=y//q
    z=min(r,s)
    if z>=d:
        print("YES")
    else:
        print("NO")