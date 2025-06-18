# cook your dish here
import math
t=int(input())
for _ in range(t):
    x = int(input())
    l=[]
    for i in range(1, int(math.sqrt(x)) + 1):
        k=i*i
        l.append(k)
    print(l[-1])