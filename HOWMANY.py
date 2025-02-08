# cook your dish here
n=int(input())
rev=0
c=0
while n!=0:
    rem=n%10;
    rev=rev*10+rem
    n=n//10
    c=c+1
if c==1:
    print("1")
if c==2:
    print("2")
if c==3:
    print("3")
if c>3:
    print("More than 3 digits")