t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=y*z
    if k>=x:
        print("Yes")
    else:
        print("No")