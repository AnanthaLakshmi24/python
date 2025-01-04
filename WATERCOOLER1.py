
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    k=x*z
    if k<y:
        print("YES")
    else:
        print("NO")