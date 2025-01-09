# cook your dish here
t=int(input())
for i in range(t):
    max=0
    mom=0
    for i in range(1,23):
        a,b=map(int,input().split())
        p=a+20*b 
        if p>max:
            max=p
            mom=i 
    print(mom)