# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if 5*x >=y:
        print("YES")
    else:
        print("NO")