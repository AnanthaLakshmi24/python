# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    z=max(x,y,z)
    p=min(x,y,z)
    diff=z-p
    print(diff)