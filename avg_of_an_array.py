li= [2,4,6,7,3,9]
sum=0
le=len(li)
for i in range(le):
    sum=sum+li[i]

avg=(sum/le)

print("{:.2f}".format(avg))