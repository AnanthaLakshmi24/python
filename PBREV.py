# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    c=0
    for i in range(len(li)):
        if li[i]>4:
            c=c+1
        else:
            c=0
    if c==n:
        print("YEs")
    else:
        print("NO")