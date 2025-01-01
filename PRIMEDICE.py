# cook your dish here
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1 
    if c==2:
        return "Alice" 
    else:
        return "Bob"
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    k=x+y
    result=prime(k)
    print(result)
    