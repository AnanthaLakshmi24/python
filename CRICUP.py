# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    diff=abs(x-y)
    if diff<=z:
        print("YES")
    else:
        print("NO")