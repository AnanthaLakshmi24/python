# cook your dish here
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().strip().split()))
    m=0
    for i in l:
        m=max(l.count(i),m)
    print(n-m)