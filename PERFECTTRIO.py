# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if (x+y)==z or (y+z)==x or (x+z)==y:
        print("YES")
    else:
        print("NO")