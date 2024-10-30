# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    x=[]
    even=0
    odd=0
    for i in range(1,n+1):
        if (n%i==0):
            x.append(i)
    for j in range(len(x)):
        if x[j]%2==0:
            even=even+1
        else:
            odd=odd+1
    if even>odd:
        print(1)
    elif even<odd:
        print(-1)
    else:
        print(0)
    