# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    k=x+y
    p=21-k 
    if p>=1 and p<=10:
        print(p)
    else:
        print(-1)