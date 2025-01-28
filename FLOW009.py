# cook your dish here

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=a*b*0.1
    if(a<=1000):
        print(a*b)
    else:
        print(a*b-c)
    
