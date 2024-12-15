# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    n=x+y
    s=500-(x*2)
    m=1000-(n*4)
    z=s+m
    a=1000-(y*4)
    b=500-(n*2)
    p=a+b 
    if z>p:
        print(z)
    elif z==p:
        print(max(z,p))
    else:
        print(p)