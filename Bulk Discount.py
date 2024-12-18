# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    amount=0
    for j in range(n):
        c=max(0,l[j]-j)
        amount=amount+c
    print(amount)