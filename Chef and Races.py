# cook your dish here
t=int(input())
for i in range(t):
    x,y,a,b=map(int,input().split())
    g_m=2
    if x==a or x==b:
        g_m=g_m-1
    if y==a or y==b:
        g_m-=1 
    print(g_m)