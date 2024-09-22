# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    li=list(map(str,input().split()))
    c=0
    d=0
    for j in range(len(li)):
        p=li[j]
        if p=="START38":
            c=c+1 
        elif p=="LTIME108":
            d=d+1 
    print(c,d)
    