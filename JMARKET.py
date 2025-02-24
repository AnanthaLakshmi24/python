# cook your dish here
for i in range(int(input())):
    x,a,b,c=map(int,input().split())
    m=min(a,b,c)
    n=max(a,b,c)
    print((x-1)*m+(a+b+c-m-n))