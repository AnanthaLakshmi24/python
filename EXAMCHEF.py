# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    p=x*y  
    if z >p/2:
        print("YES")
    else:
        print("NO")