import math
n=int(input())
for i in range(1,32,1):
    if math.pow(3,i) == n:
          print("YEs")
          break
else:
    print("No")