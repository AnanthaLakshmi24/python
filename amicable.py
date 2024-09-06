n=int(input())
m=int(input())
c=0
sum=0
boom=0
for i in range(1,n+1,1):
    if n%i==0:
         sum=sum+i

for x in range(1,m+1,1):
    if m%x==0:
        boom=boom+x
if sum==boom:
    print("Amicable Number")
else:
    print("Not Amicable Number")