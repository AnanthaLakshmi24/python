import math
# cook your dish here
t=int(input())
for i in range(t):
    x1,y1,x2,y2=map(int,input().split())
    p=((x1)*(x1) + (y1)*(y1))
    q=((x2)*(x2) + (y2)*(y2))
    alex=math.sqrt(p)
    bob=math.sqrt(q)
    if alex>bob:
        print("ALEX")
    elif alex==bob:
        print("EQUAL")
    else:
        print("BOB")