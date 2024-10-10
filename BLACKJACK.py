# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    z=x+y 
    p=21-z
    if p>=1 and p<=10:
        print(p)
    else:
        print(-1)
    