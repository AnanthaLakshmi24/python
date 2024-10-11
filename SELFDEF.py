# cook your dish here
t=int(input())
for i in range(t):
    x=int(input())
    li=list(map(int,input().split()))
    c=0
    for j in range(len(li)):
        if li[j]>=10 and li[j]<=60:
            c=c+1 
    print(c)