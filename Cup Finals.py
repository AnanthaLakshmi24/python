# cook your dish here
t=int(input())
for i in range(t):
    x,y,d=map(int,input().split())
    k=abs(x-y)
    if k<=d:
        print("YES")
    else:
        print("NO")