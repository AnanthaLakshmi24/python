# cook your dish here
for i in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    for i in range(-1,-(n+1),-1):
        if a[i] >= x:
            c+=1
        elif a[i] < x:
            break
    print(n-c)