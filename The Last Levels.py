# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x%3!=0:
        k=(x//3 )
    else:
        k=(x//3)-1
    p=((x*y)+(k*z))
    print(p)
        