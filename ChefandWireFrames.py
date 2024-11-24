# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=(2*x)+(2*y)
    print(z*k)