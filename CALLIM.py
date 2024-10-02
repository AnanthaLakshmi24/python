# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    li=list(map(int,input().split()))
    sum=0
    c=0
    for j in range(len(li)):
        sum=sum+li[j]
        if sum>y:
            break
        c=c+1 
    print(c)