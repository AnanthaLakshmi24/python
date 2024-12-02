# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=x*y 
    if z>k/2:
        print("YES")
    else:
        print("NO")