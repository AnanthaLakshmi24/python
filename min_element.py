x=[2,5,4,1,9,6]
le=len(x)
min=100000000
for i in range(1,le,1):
    if min>x[i]:
        min=x[i]
print(min)