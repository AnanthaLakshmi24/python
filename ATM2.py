# cook your dish here
t=int(input())
for j in range(t):
    x,y=map(int,input().split())
    li=list(map(int,input().split()))
    ns=""
    for i in range(x):
        if li[i]<=y:
            ns=ns+"1"
            y=y-li[i]
        else:
            ns=ns+"0"
            
    print(ns)
          
        