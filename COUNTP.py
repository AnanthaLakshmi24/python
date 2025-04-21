# cook your dish here
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    f=c=0
    for i in a:
        if(i%2==1):
            c+=1
    if(c%2==1 or c==0):
        print('NO')
    else:
        print('YES')