# cook your dish here
import math
T = int(input())

for i in range(T):
    L, V1, V2 = map(int, input().split())
    
    t1 = math.ceil(L / V1)
    t2 = math.ceil(L / V2)

    if t1 == t2:
        print(-1)
    elif(t1-1 == t2):
        print(0)
    else:
        print(t1-t2-1)
    
        