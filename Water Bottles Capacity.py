# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=z//y
    if k<=x:
        print(k)
    else:
        print(x)