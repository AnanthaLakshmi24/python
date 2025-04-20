# cook your dish here
for _ in range(int(input())):
    e,k=map(int,input().split())
    c=0
    while e>0:
        e=e//k
        c+=1
    print(c)    