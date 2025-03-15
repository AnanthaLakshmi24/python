# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=0
    for i in range(n):
        if i==0:
            if a[i]>=b[i]:
                ans+=1 
        else:
            if a[i]-a[i-1]>=b[i]:
                ans+=1 
    print(ans)