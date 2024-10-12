# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    p=x*y  
    if p<=z:
        print(0)
    else:
        print((p-z+y-1)//y)
                