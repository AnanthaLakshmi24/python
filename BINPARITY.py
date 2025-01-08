# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    b=bin(n)
    k=b.count("1")
    if k%2==0:
        print("EVEN")
    else:
        print("ODD")