# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    z=min(20,x//y) 
    print(z)