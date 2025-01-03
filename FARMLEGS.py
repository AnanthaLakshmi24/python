# cook your dish here
import math
t=int(input())
for i in range(t):
    x=int(input())
    cow=x//4 
    if x%4!=0:
        print(cow+1)
    else:
        print(cow)