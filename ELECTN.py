# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    li=list(map(int,input().split()))
    c=0
    for j in range(len(li)):
        if y<=li[j]:
            c=c+1
    print(c)