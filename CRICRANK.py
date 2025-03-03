# cook your dish here
for i in range(int(input())):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ca,cb=0,0
    for i in range(3):
        if a[i]>b[i]:
            ca+=1
        elif a[i]<b[i]:
            cb+=1
    if ca>cb:
        print('A')
    elif ca<cb:
        print('B')
        