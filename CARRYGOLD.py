# cook your dish here
t=int(input())
for i in range(t):
    n, x, y=map(int, input().split())
    if((n+1)*y>=x):
        print("yes")
    else:
        print("no")