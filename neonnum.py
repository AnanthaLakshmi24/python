#sum of squares is equals to given num
n=int(input())
temp=n
s=0
sqr=n*n
while(sqr>0):
    rem=sqr%10
    s=s+rem
    n=n//10

if s==temp:
    print("Neon number")
else:
    print("Not a NEon number")