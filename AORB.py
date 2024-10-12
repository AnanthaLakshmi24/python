# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    k=x
    l=x+y 
    a=500-(k*2)
    b=1000-(l*4)
    sum=a+b 
    j=y    
    p=x+y   
    c=1000-(j*4)
    d=500-(p*2)
    total=c+d 
    if sum>total:
        print(sum)
    else:
        print(total)