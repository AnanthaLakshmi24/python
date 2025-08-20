# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    b=0
    r=0
    u=0
    for i in l:
        if i ==1:
            r=r+1
        if i==2:
            b=b+1
        if i==0:
            u=u+1
    while u>0:
        if b>r:
            r=r+1
        else:
            b=b+1
        u=u-1
    
    if b==r:
        print("Yes")
    else:
        print("No")
        
        