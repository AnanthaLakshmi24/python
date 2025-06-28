# cook your dish here
for i in range(int(input())):
    x,p,q=map(int,input().split())
    if(p>q):
        p=p-q
        print(p*x)
    else:
        print(0)