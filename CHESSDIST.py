# cook your dish here
t=int(input())
for _ in range(t):
    x1,y1,x2,y2=map(int,input().split())
    p=abs(x1-x2)
    q=abs(y1-y2)
    r=max(p,q)
    print(r)
            