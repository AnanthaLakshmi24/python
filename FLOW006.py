# cook your dish here
t=int(input())
for i in range (t):
    x=int(input())
    sum=0
    rev=0
    while x!=0:
        rem=x%10
        sum=sum+rem
        rev=(rev*10)+rem
        x=x//10
    
    print(sum)