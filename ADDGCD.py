# cook your dish here
import math 
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    k = math.gcd(x,y)
    if k>1:
        print(0)
    else:
        if math.gcd(x+1,y)>1 or math.gcd(x,y+1)>1:
            print(1)
        else:
            print(2)
        