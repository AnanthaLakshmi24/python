# cook your dish here
for i in range(int(input())):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c1a,c1b=0,0
    for i in a:
        if i==1:
            c1a+=1
    for i in b:
        if i==1:
            c1b+=1
    if c1a==c1b:
        print('Pass')
    else:
        print('Fail')