# cook your dish here
t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    min_diff=abs(2*(1+1)-k)
    for l in range(1,n+1):
        for w in range(1,m+1):
            peri=2*(l+w)
            diff = abs(peri-k)
            if diff < min_diff:  
                min_diff = diff
    print(min_diff)