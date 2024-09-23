# cook your dish here
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    z=x-y
    if z<=y:
        print("YES")
    else:
        print("NO")