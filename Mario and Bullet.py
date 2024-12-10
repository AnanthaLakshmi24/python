# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=y//x
    if (z-k)>=0:
        print(z-k)
    else:
        print(0)