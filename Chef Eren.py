# cook your dish here
t=int(input())
for i in range(t):
    k,a,b=map(int,input().split())
    e=k//2
    o=k-e
    p=((e*a)+(o*b))
    print((p))
        