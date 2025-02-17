# cook your dish here
t=int(input())
for i in range(0,t):
    n,m=map(int,input().split())
    if m>n:
        y=m%n
        x=m//n
        z=n*(x+1)
        if y==0:
            print(0)
        elif ((z-m)>y):
            print(y)
        else:
            print(z-m)
    else:
        print(n-m)
    
    