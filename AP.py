# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    p=(2*y)
    q=(x+z)
    if p==q:
        print(0)
    else:
        print(1)