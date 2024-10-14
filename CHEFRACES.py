# cook your dish here
t=int(input())
for i in range(t):
    x,y,a,b=map(int,input().split())
    c=0
    if x!=a and x!=b:
        c=c+1
    if y!=a and y!=b:
        c=c+1
    print(c)