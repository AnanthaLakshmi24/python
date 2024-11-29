# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=x*10
    if y<=k:
        print(y*z)
    else:
        print(k*z)