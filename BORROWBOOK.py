# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    res=0
    unique_days=set(l)
    l=l[::-1]
    for i in unique_days:
        res+=(n- l.index(i))
    print(res)