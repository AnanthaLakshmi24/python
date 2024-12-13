# cook your dish here
t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split())
    if w==x or w==y or w==z or (x+y)==w or (x+z)==w or (y+z)==w or (x+y+z)==w:
        print("YES")
    else:
        print("NO")