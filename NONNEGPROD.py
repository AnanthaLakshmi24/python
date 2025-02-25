# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    c=0
    p=1
    for k in range(n):
        p=p*a[k]
        
    if(p>=0):
        print(0)
    else:
        print(1)