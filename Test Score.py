# cook your dish here
t=int(input())
for i in range(t):
    n,x,y=map(int,input().split())
    if y==0:
        print("YES")
    else:
        if y%x==0 and (y//x) <= n:
            print("YES")
        else:
            print("NO")