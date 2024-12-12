# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>=y:
        k=x//y 
        p=abs(x-(y*k))
        print(k+p)
    else:
        print(x)