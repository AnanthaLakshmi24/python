# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    area=x*y
    cost=2*area 
    max_walls=z//cost
    print(max_walls)