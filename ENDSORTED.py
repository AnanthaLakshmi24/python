# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=l.index(1)
    N=l.index(n)
    b=(n-1)-N
    if a<N:
        print(a+b)
    else:
        print(a+b-1)