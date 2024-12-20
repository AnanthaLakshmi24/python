# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    for i in range(1,n+1,1):
        if n % i == 0:
            c=c+1
    if c==2:
        print("yes")
    else:
        print("no")