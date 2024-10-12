# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())  
    p=2**(x-n)
    print(p)