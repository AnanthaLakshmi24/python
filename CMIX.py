# cook your dish here
for _ in range(int(input())):
    n = int(input())
    v,a = [0]*n,[0]*n
    for i in range(n):
        v[i],a[i] = map(int,input().split())
    ms = 0
    for i in range(n):
        for j in range(i+1,n):
            Stren = a[i]*v[j]+v[i]*a[j]
            ms = max(ms, Stren)
    print(ms)
            
    
        
        
        
        