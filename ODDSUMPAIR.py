t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if ((x+y)%2==1) or ((y+z)%2==1) or ((x+z)%2==1) :
        print("YES")
    else:
        print("NO")