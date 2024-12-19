# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=x+y+z 
    p=min(x,y,z)
    print(k-p)