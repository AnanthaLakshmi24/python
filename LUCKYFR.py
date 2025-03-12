# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    rev=0 
    c=0
    while n!=0:
        rem=n%10;
        if rem==4:
            c=c+1 
        n=n//10
    print(c)