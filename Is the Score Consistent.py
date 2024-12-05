# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    if a>=x and b>=y:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")