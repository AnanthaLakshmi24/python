# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    p=abs(x/y)
    if p%2==0:
        print("Yes")
        
    else:print("No")