# cook your dish here
x,y,z=map(int,input().split())
s=(x+y+z)
if (x+4-s)>z:
    print("Yes")
else:
    print("No")