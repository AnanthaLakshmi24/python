# cook your dish here
for i in range(int(input())):
    n,a,b=map(int,input().split())
    x=list(map(int,input().split()))
    na=x.count(a)/n
    nb=x.count(b)/n
    print(na*nb)