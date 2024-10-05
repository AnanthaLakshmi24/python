# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z,c=map(int,input().split())
    if (x+y>=c) or (x+z>=c) or (y+z>=c):
        print("YES")
    else:
        print("NO")