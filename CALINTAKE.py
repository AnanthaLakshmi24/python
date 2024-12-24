# cook your dish here
x,y,z=map(int,input().split())
k=y*z 
if (x-k)>=0:
    print(x-k)
else:
    print(-1)