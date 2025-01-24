# cook your dish here
import math
t = int(input())

for i in range(t):
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    
    total = sum(A)
    
    min_bottle = math.ceil(total/X)
    print(min_bottle)