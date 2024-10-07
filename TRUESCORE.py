# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    p,q=map(int,input().split())
    if x<=p and y<=q:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")