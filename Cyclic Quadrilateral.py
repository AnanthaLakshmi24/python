# cook your dish here
t=int(input())
for i in range(t):
    a,x,b,y=map(int,input().split())
    k=a+b 
    p=x+y
    if k==180 and p==180:
        print("YES")
    else:
        print("NO")