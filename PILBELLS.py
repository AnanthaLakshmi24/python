# cook your dish here
t =int(input())
for i in range(t):
    n,x,k,p = list(map(int,input().split()))
    if(n==k):
        p += ((x*10)+((k-x)*5)+20)
    else:
        if(x>=k):
            p += k*10
        else:
            p += ((x*10)+((k-x)*5))
    print(p)
            
        
