t=int(input())
for i in range(t):
    a,b,x=map(int,input().split())
    z=abs(a-b)
    years=z//x 
    print(years)