import math
# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    per=0.2*x
    earn=100/per
    print(math.ceil(earn))