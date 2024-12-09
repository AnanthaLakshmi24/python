# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    k=abs(y-x)
    if k>=y:
        print(y)
    else:
        print(k)
    