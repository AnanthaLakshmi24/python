# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    c=0
    li=list(map(int,input().split()))
    for i in li:
        c=c+((i+1)//2)
    print(c)
            