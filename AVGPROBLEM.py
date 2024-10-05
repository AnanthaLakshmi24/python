# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    avg=(x+y)/2
    if avg>z:
        print("YES")
    else:
        print("NO")