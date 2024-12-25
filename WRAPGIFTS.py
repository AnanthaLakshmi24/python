# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=(x*y)+(y*z)+(z*x)
    print(1000//(2*k))