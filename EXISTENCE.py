# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    k=(x**4)+(4*(y**2))
    s=4*(x**2)*y
    if k==s:
        print("YES")
    else:
        print("NO")