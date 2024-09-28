# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    extra_shoes=x+max(0,x-y)
    print(extra_shoes)