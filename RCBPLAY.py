# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    max=x+2*z
    if max>=y:
        print("YES")
    else:
        print("NO")