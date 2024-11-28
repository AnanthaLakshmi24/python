# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>=30*y:
        print("YES")
    else:
        print("NO")