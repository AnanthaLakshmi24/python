# cook your dish here

from math import ceil

for T in range(int(input())):
    
    A,B = map(int,input().split())
    
    if A >= B + 10:
        print(0)
        
    else:
        left  = B + 10 - A
        shots = ceil(left/3)
        print(shots)
        
