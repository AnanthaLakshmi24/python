# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    z=y-x
    if z%2==0:
        print("YES")
    else:
        print("NO")