# cook your dish here
t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    k=c//a 
    p=d//b 
    print(k+p)