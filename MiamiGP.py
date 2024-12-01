# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if y<=(x*1.07):
        print("YES")
    else:
        print("NO")