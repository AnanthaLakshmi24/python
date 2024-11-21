# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    z=x+1
    if z<=y:
        print("YES")
    else:
        print("NO")