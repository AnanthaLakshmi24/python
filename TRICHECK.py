# cook your dish here
x,y,z=map(int,input().split())
if (x+y>z) and (y+z>x) and (x+z>y):
    print("YES")
else:
    print("NO")