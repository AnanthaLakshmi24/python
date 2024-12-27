for _ in range(int(input())):

    n=int(input())
    a=list(map(int,input().split()))
    
    mx=a[-1]
    c=0
    ans=0
    for i in range(n-2,-1,-1):
        if a[i]<mx:
            a[i]=mx
            c+=1
        else:
            mx=a[i]
            c=0
        ans=max(ans,c)
            
    print(ans)
            