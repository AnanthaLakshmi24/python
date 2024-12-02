# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=(x+y)/2
    if k>z:
        print("YES")
    else:
        print("NO")