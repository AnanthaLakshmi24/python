li= [2,4,6,7,3,9]
sum=0
c=0
le=len(li)
for i in range(le):
    sum=sum+li[i]

avg=(sum/le)

for j in range(le):
    if avg<=li[j]:
        c=c+1
print(c)