# cook your dish here
t=int(input())
for i in range(t):
    a,b,x,y=map(int,input().split())
    k=a*b 
    p=x*y
    if p>=k:
        print("YES")
    else:
        print("NO")