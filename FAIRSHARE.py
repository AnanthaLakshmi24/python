# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    f=k+1
    a=n//f 
    s=k*a
    print(n-s)