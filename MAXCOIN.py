# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    a=[]
    s=0
    for i in range(1,n+1):
        a.append(2**i)
    for i in range(x):
        s+=a.pop()
    print(s-sum(a))