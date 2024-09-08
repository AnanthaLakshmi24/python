num=int(input())
sum=0
while(num!=0):
        rem=num%10
        sum=sum+rem
        num=num//10

if(sum<=9):
    print(sum)
else:
     print((sum-1)%9+1)
