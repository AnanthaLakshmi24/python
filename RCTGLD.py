# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    if n<4:
        print(0)
    else:
        s=n//2
        p=s//2
        if s%2==0:
            print(p*p)
        else:
            print(p*(p+1))
        
            