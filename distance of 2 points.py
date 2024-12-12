# cook your dish here
t=int(input())
for i in range(t):
    x1,y1,x2,y2=map(int,input().split())
    k=abs(x2-x1)
    y=abs(y2-y1)
    print(max(k,y))