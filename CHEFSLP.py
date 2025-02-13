# cook your dish here
for _ in range(int(input())):
    n,l,x=map(int,input().split())
    print(x*(min(l,n-l)))