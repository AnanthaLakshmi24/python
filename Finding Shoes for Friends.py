# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    print(n+max(0,n-m))