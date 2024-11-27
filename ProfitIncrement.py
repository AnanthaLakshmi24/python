# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    z=x//10
    k=x-y
    print(x+z-k)