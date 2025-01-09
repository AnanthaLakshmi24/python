# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    k=x//2
    if k<=y:
        print(k)
    else:
        print(y)