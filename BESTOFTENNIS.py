# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    n = 2 * max(x, y) - 1
    print(n)