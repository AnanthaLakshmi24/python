# cook your dish here
import math
a = int(input())
if a >= 25:
    print(0)
else:
    years = math.ceil((25 - a) / 4)
    print(years)
