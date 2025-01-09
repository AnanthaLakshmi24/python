# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    temp=n
    rev=0
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if temp==rev:
        print("wins")
    else:
        print("loses")