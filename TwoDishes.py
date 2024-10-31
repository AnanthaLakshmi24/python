# cook your dish here
t=int(input())
for i in range(t):
    n,a,b,c=map(int,input().split())
    max=min(b,a+c)
    if max>=n:
        print("YES")
    else:
        print("NO")