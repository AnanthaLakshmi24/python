# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if ((x+y)<z) or ((x+z)<y) or ((y+z)<x):
        print("Yes")
    else:
        print("No")