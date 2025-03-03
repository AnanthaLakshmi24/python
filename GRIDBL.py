# cook your dish here
for i in range(int(input())):
    n,m=map(int,input().split())
    if n%2!=0 and m%2!=0:
        print(m+(n-1))
    elif n%2==0 and m%2==0:
        print(0)
    elif n%2==0 and m%2!=0:
        print(n)
    elif n%2!=0 and m%2==0:
        print(m)