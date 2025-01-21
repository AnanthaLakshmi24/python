# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    k=x%3
    p=y%3
    if k==p:
        print(k)
    else:
        print(0)